from django.db import models, transaction
from django.db.models import F
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta


# =========================
# 📚 BOOK MODEL
# =========================
class Book(models.Model):
    school = models.ForeignKey("School", on_delete=models.CASCADE, related_name="books")

    title = models.CharField(max_length=150, db_index=True)
    author = models.CharField(max_length=100, db_index=True)

    isbn = models.CharField(max_length=20, blank=True, null=True, db_index=True)
    publication_date = models.DateField(null=True, blank=True)

    total_copies = models.PositiveIntegerField(default=1)
    available_copies = models.PositiveIntegerField(default=1)

    CATEGORY_CHOICES = [
        ("Academic", "Academic"),
        ("Reference", "Reference"),
        ("Fiction", "Fiction"),
        ("Non-Fiction", "Non-Fiction"),
        ("Other", "Other"),
    ]
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default="Academic")

    is_active = models.BooleanField(default=True, db_index=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.total_copies <= 0:
            raise ValidationError("Total copies must be at least 1")

        if self.available_copies < 0:
            raise ValidationError("Available copies cannot be negative")

        if self.available_copies > self.total_copies:
            raise ValidationError("Available copies cannot exceed total copies")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["school", "title", "author"],
                name="unique_book_per_school"
            )
        ]
        indexes = [
            models.Index(fields=["school", "title"]),
            models.Index(fields=["school", "author"]),
        ]

    def __str__(self):
        return f"{self.title} - {self.author}"


# =========================
# 📖 BOOK ISSUE MODEL
# =========================
class BookIssue(models.Model):
    student = models.ForeignKey("Student", on_delete=models.CASCADE, related_name="book_issues")
    book = models.ForeignKey("Book", on_delete=models.CASCADE, related_name="issues")

    issue_date = models.DateField(default=timezone.now)
    due_date = models.DateField(blank=True)
    return_date = models.DateField(null=True, blank=True)

    is_returned = models.BooleanField(default=False)
    fine_amount = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    # -------------------------
    # 🔍 VALIDATIONS
    # -------------------------
    def clean(self):
        previous = getattr(self, "_previous_state", None)

        # Prevent reverting returned record
        if previous and previous.is_returned and not self.is_returned:
            raise ValidationError("Cannot revert a returned book issue")

        # Prevent editing after return
        if previous and previous.is_returned and self.is_returned:
            if self.return_date != previous.return_date:
                raise ValidationError("Returned records cannot be modified")

        # Require return_date when returning
        if self.is_returned and not self.return_date:
            raise ValidationError("Return date is required")

        # Same school validation
        if self.student.school != self.book.school:
            raise ValidationError("Student and Book must belong to same school")

        # Auto due date
        if not self.due_date:
            self.due_date = self.issue_date + timedelta(days=14)

        # Date validations
        if self.due_date < self.issue_date:
            raise ValidationError("Due date cannot be before issue date")

        if self.return_date and self.return_date < self.issue_date:
            raise ValidationError("Return date cannot be before issue date")

        # Prevent issuing if no copies available
        if not self.pk and self.book.available_copies <= 0:
            raise ValidationError("No copies available")

        # Limit books per student
        active = BookIssue.objects.filter(
            student=self.student,
            is_returned=False
        ).exclude(pk=self.pk).count()

        if active >= 3:
            raise ValidationError("Max 3 books allowed")

    # -------------------------
    # 💰 FINE CALCULATION
    # -------------------------
    @property
    def calculate_fine(self):
        if self.return_date and self.return_date > self.due_date:
            return (self.return_date - self.due_date).days * 5
        return 0

    # -------------------------
    # 🔁 SAVE LOGIC (SAFE)
    # -------------------------
    def save(self, *args, **kwargs):
        with transaction.atomic():

            if self.pk:
                self._previous_state = BookIssue.objects.select_for_update().get(pk=self.pk)

            is_new = self.pk is None

            # 📉 Issue
            if is_new:
                book = Book.objects.select_for_update().get(pk=self.book.pk)

                if book.available_copies <= 0:
                    raise ValidationError("No copies available")

                book.available_copies = F('available_copies') - 1
                book.save()
                book.refresh_from_db()

            # 📈 Return
            if self.is_returned and self.return_date:
                prev = getattr(self, "_previous_state", None)

                if not prev or not prev.is_returned:
                    book = Book.objects.select_for_update().get(pk=self.book.pk)

                    book.available_copies = F('available_copies') + 1
                    book.save()
                    book.refresh_from_db()

                self.fine_amount = self.calculate_fine

            self.full_clean()
            super().save(*args, **kwargs)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["student", "book"],
                condition=models.Q(is_returned=False),
                name="unique_active_book_per_student"
            )
        ]
        indexes = [
            models.Index(fields=["student"]),
            models.Index(fields=["book"]),
            models.Index(fields=["student", "is_returned"]),
            models.Index(fields=["due_date", "is_returned"]),
        ]
        ordering = ["-created_at"]  # ✅ Latest first

    def __str__(self):
        return f"{self.student} → {self.book.title}"