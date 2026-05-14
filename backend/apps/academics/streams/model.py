from django.db import models


class Stream(models.Model):

    school = models.ForeignKey(
        "schools.School",
        on_delete=models.CASCADE,
        related_name="streams",
        db_index=True
    )

    name = models.CharField(
        max_length=100
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

        constraints = [

            models.UniqueConstraint(
                fields=["school", "name"],
                name="unique_stream_per_school"
            )
        ]

    def __str__(self):

        return self.name