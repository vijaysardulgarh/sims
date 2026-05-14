from django.db import models


class Class(models.Model):

    school = models.ForeignKey(
        "schools.School",
        on_delete=models.CASCADE,
        related_name="classes",
        db_index=True
    )

    name = models.CharField(
        max_length=50
    )

    class_order = models.PositiveIntegerField(
        default=0
    )

    def clean(self):

        if self.name:
            self.name = (
                self.name.strip().upper()
            )

    def save(self, *args, **kwargs):

        self.full_clean()

        super().save(*args, **kwargs)

    class Meta:

        ordering = [
            "class_order",
            "name"
        ]

        constraints = [

            models.UniqueConstraint(
                fields=["school", "name"],
                name="unique_class_per_school"
            )
        ]

    def __str__(self):

        return self.name