from django.db import models

class FAQ(models.Model):
    CATEGORY_CHOICES = [
        ("admission", "Admission"),
        ("fees", "Fees & Payments"),
        ("academics", "Academics"),
        ("facilities", "Facilities"),
        ("general", "General"),
    ]

    question = models.CharField(max_length=300, help_text="Enter the FAQ question")
    answer = models.TextField(help_text="Provide the answer for the question")
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default="general",
        help_text="Select category of FAQ"
    )
    order = models.PositiveIntegerField(default=0, help_text="Order for display (0 = top)")
    is_active = models.BooleanField(default=True, help_text="Show or hide on website")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "category", "id"]

    def __str__(self):
        return self.question