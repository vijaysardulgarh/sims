from django.db import models


class Day(
    models.Model
):

    school = models.ForeignKey(
        "schools.School",
        on_delete=models.CASCADE,
        related_name="days",
        db_index=True
    )

    name = models.CharField(
        max_length=20,
        db_index=True
    )

    sequence = models.PositiveIntegerField()

    class Meta:

        ordering = [
            "sequence"
        ]

        constraints = [

            models.UniqueConstraint(
                fields=[
                    "school",
                    "name"
                ],
                name="unique_day_per_school"
            ),

            models.UniqueConstraint(
                fields=[
                    "school",
                    "sequence"
                ],
                name="unique_day_sequence_per_school"
            )
        ]

    def clean(self):

        if self.name:

            self.name = (
                self.name.strip().title()
            )

    def save(self, *args, **kwargs):

        self.full_clean()

        super().save(*args, **kwargs)

    def __str__(self):

        return self.name