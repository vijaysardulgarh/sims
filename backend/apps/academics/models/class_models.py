from django.db import models
from django.core.exceptions import ValidationError
from django.db.models import Q


# =========================================
# CLASS
# =========================================

class Class(models.Model):

    school = models.ForeignKey(
        "schools.School",
        on_delete=models.CASCADE,
        related_name="classes",
        db_index=True
    )

    name = models.CharField(max_length=50)

    class_order = models.PositiveIntegerField(
        default=0
    )

    def clean(self):

        if self.name:
            self.name = self.name.strip().upper()

    def save(self, *args, **kwargs):

        self.full_clean()

        super().save(*args, **kwargs)

    class Meta:

        constraints = [

            models.UniqueConstraint(
                fields=["school", "name"],
                name="unique_class_per_school"
            )
        ]

        ordering = ["class_order", "name"]

    def __str__(self):

        return self.name


# =========================================
# STREAM
# =========================================

class Stream(models.Model):

    name = models.CharField(max_length=100)

    school = models.ForeignKey(
        "schools.School",
        on_delete=models.CASCADE,
        related_name="streams",
        db_index=True
    )

    def clean(self):

        if self.name:
            self.name = self.name.strip().upper()

    def save(self, *args, **kwargs):

        self.full_clean()

        super().save(*args, **kwargs)

    class Meta:

        constraints = [

            models.UniqueConstraint(
                fields=["school", "name"],
                name="unique_stream_per_school"
            )
        ]

    def __str__(self):

        return self.name


# =========================================
# MEDIUM
# =========================================

class Medium(models.Model):

    name = models.CharField(max_length=50)

    school = models.ForeignKey(
        "schools.School",
        on_delete=models.CASCADE,
        related_name="mediums",
        db_index=True
    )

    def clean(self):

        if self.name:
            self.name = self.name.strip().upper()

    def save(self, *args, **kwargs):

        self.full_clean()

        super().save(*args, **kwargs)

    class Meta:

        constraints = [

            models.UniqueConstraint(
                fields=["school", "name"],
                name="unique_medium_per_school"
            )
        ]

    def __str__(self):

        return self.name


# =========================================
# CLASSROOM
# =========================================

class Classroom(models.Model):

    school = models.ForeignKey(
        "schools.School",
        on_delete=models.CASCADE,
        related_name="classrooms",
        db_index=True
    )

    name = models.CharField(max_length=20)

    capacity = models.PositiveIntegerField(
        default=40
    )

    floor = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    def clean(self):

        if self.name:
            self.name = self.name.strip().upper()

        if self.capacity <= 0:
            raise ValidationError(
                "Capacity must be greater than 0"
            )

    def save(self, *args, **kwargs):

        self.full_clean()

        super().save(*args, **kwargs)

    class Meta:

        constraints = [

            models.UniqueConstraint(
                fields=["school", "name"],
                name="unique_classroom_per_school"
            )
        ]

    def __str__(self):

        return f"Room {self.name}"


# =========================================
# SECTION
# =========================================

class Section(models.Model):

    SUB_STREAM_CHOICES = [

        ("Medical", "Medical"),

        ("Non-Medical", "Non-Medical"),

        ("Vocational", "Vocational"),
    ]

    school = models.ForeignKey(
        "schools.School",
        on_delete=models.CASCADE,
        related_name="sections",
        db_index=True
    )

    class_obj = models.ForeignKey(
        Class,
        on_delete=models.CASCADE,
        related_name="sections",
        db_index=True
    )

    name = models.CharField(max_length=10)

    classroom = models.ForeignKey(
        Classroom,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="sections"
    )

    medium = models.ForeignKey(
        Medium,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="sections"
    )

    stream = models.ForeignKey(
        Stream,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="sections"
    )

    sub_stream = models.CharField(
        max_length=100,
        choices=SUB_STREAM_CHOICES,
        null=True,
        blank=True
    )

    def clean(self):

        if self.name:
            self.name = self.name.strip().upper()

        if self.sub_stream and not self.stream:
            raise ValidationError(
                "Sub-stream requires a stream"
            )

    def save(self, *args, **kwargs):

        self.full_clean()

        super().save(*args, **kwargs)

    class Meta:

        ordering = [
            "class_obj__class_order",
            "name"
        ]

    def __str__(self):

        return self.name
