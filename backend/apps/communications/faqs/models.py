class FAQ(models.Model):
   

    CATEGORY_CHOICES = [
        ("admission", "Admission"),
        ("fees", "Fees"),
        ("academics", "Academics"),
        ("facilities", "Facilities"),
        ("general", "General"),
    ]

    question = models.CharField(max_length=300)
    answer = models.TextField()

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default="general")

    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.question:
            self.question = self.question.strip()
        if self.answer:
            self.answer = self.answer.strip()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["school", "question"], name="unique_faq_per_school")
        ]
        ordering = ["order", "category"]
        indexes = [
            models.Index(fields=["school", "category"]),
        ]

    def __str__(self):
        return self.question