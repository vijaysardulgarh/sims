from django.db import models

from django.core.exceptions import (
    ValidationError
)

from django.db.models.functions import (
    Lower
)

from apps.core.common.base.models import (
    SchoolBaseModel
)


class Subject(SchoolBaseModel):

    # ============================================
    # BASIC
    # ============================================

    name = models.CharField(
        max_length=100,
        db_index=True
    )

    code = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        db_index=True
    )

    # ============================================
    # FLAGS
    # ============================================

    is_language = models.BooleanField(
        default=False
    )

    is_optional = models.BooleanField(
        default=False
    )

    has_lab = models.BooleanField(
        default=False
    )

    # ============================================
    # META
    # ============================================

    class Meta:

        db_table = "subjects"

        ordering = [
            "name"
        ]

        constraints = [

            models.UniqueConstraint(

                Lower("name"),

                "school",

                name=(
                    "unique_subject_per_school_"
                    "case_insensitive"
                )
            )
        ]

    # ============================================
    # VALIDATION
    # ============================================

    def clean(self):

        if (

            self.name

            and

            Subject.objects.exclude(
                pk=self.pk
            ).filter(

                school=self.school,

                name__iexact=self.name

            ).exists()
        ):

            raise ValidationError({

                "name":
                    "This subject already exists."
            })

    # ============================================
    # SAVE
    # ============================================

    def save(
        self,
        *args,
        **kwargs
    ):

        if self.name:

            self.name = (
                self.name.strip().title()
            )

        if self.code:

            self.code = (
                self.code.strip().upper()
            )

        self.full_clean()

        super().save(
            *args,
            **kwargs
        )

    # ============================================
    # STRING
    # ============================================

    def __str__(self):

        return self.name