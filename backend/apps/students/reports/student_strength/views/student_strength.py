from django.db.models import Count
from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.response import Response

from apps.students.profiles.models import Student

from ..serializers.student_strength import (
    StudentStrengthSerializer
)


class StudentStrengthAPIView(
    APIView
):

    def get(self, request):

        queryset = (

            Student.objects

            .filter(
                student_class__isnull=False,
                section__isnull=False,
            )

            .values(
                "student_class__name",
                "section__name",
            )

            .annotate(

                sc_male=Count(
                    "srn",
                    filter=Q(
                        category="SC",
                        gender__iexact="Male",
                    )
                ),

                sc_female=Count(
                    "srn",
                    filter=Q(
                        category="SC",
                        gender__iexact="Female",
                    )
                ),

                bca_male=Count(
                    "srn",
                    filter=Q(
                        category="BC-A",
                        gender__iexact="Male",
                    )
                ),

                bca_female=Count(
                    "srn",
                    filter=Q(
                        category="BC-A",
                        gender__iexact="Female",
                    )
                ),

                bcb_male=Count(
                    "srn",
                    filter=Q(
                        category="BC-B",
                        gender__iexact="Male",
                    )
                ),

                bcb_female=Count(
                    "srn",
                    filter=Q(
                        category="BC-B",
                        gender__iexact="Female",
                    )
                ),

                gen_male=Count(
                    "srn",
                    filter=Q(
                        category="GEN",
                        gender__iexact="Male",
                    )
                ),

                gen_female=Count(
                    "srn",
                    filter=Q(
                        category="GEN",
                        gender__iexact="Female",
                    )
                ),

            )

            .order_by(
                "student_class__display_order",
                "section__name",
            )

        )

        result = []

        grand_total = {

            "sc_male": 0,
            "sc_female": 0,

            "bca_male": 0,
            "bca_female": 0,

            "bcb_male": 0,
            "bcb_female": 0,

            "gen_male": 0,
            "gen_female": 0,

        }

        current_class = None

        class_total = None

        for row in queryset:

            class_name = (
                row["student_class__name"]
            )

            if (
                current_class
                and current_class != class_name
            ):

                result.append(
                    self.build_total_row(
                        current_class,
                        class_total,
                        "class_total",
                    )
                )

                class_total = None

            if class_total is None:

                class_total = {

                    "sc_male": 0,
                    "sc_female": 0,

                    "bca_male": 0,
                    "bca_female": 0,

                    "bcb_male": 0,
                    "bcb_female": 0,

                    "gen_male": 0,
                    "gen_female": 0,

                }

            current_class = class_name

            section_row = self.build_section_row(
                row
            )

            result.append(
                section_row
            )

            for field in class_total:

                class_total[field] += (
                    row[field]
                )

                grand_total[field] += (
                    row[field]
                )

        if current_class:

            result.append(
                self.build_total_row(
                    current_class,
                    class_total,
                    "class_total",
                )
            )

        result.append(
            self.build_total_row(
                "",
                grand_total,
                "grand_total",
            )
        )

        serializer = (
            StudentStrengthSerializer(
                result,
                many=True
            )
        )

        return Response(
            serializer.data
        )

    def build_section_row(
        self,
        row
    ):

        sc_total = (
            row["sc_male"] +
            row["sc_female"]
        )

        bca_total = (
            row["bca_male"] +
            row["bca_female"]
        )

        bcb_total = (
            row["bcb_male"] +
            row["bcb_female"]
        )

        gen_total = (
            row["gen_male"] +
            row["gen_female"]
        )

        overall_male = (

            row["sc_male"] +
            row["bca_male"] +
            row["bcb_male"] +
            row["gen_male"]

        )

        overall_female = (

            row["sc_female"] +
            row["bca_female"] +
            row["bcb_female"] +
            row["gen_female"]

        )

        return {

            "row_type": "section",

            "class_name":
                row["student_class__name"],

            "section_name":
                row["section__name"],

            "sc_male":
                row["sc_male"],

            "sc_female":
                row["sc_female"],

            "sc_total":
                sc_total,

            "bca_male":
                row["bca_male"],

            "bca_female":
                row["bca_female"],

            "bca_total":
                bca_total,

            "bcb_male":
                row["bcb_male"],

            "bcb_female":
                row["bcb_female"],

            "bcb_total":
                bcb_total,

            "gen_male":
                row["gen_male"],

            "gen_female":
                row["gen_female"],

            "gen_total":
                gen_total,

            "overall_male":
                overall_male,

            "overall_female":
                overall_female,

            "overall_total":
                overall_male +
                overall_female,

        }

    def build_total_row(
        self,
        class_name,
        totals,
        row_type,
    ):

        sc_total = (
            totals["sc_male"] +
            totals["sc_female"]
        )

        bca_total = (
            totals["bca_male"] +
            totals["bca_female"]
        )

        bcb_total = (
            totals["bcb_male"] +
            totals["bcb_female"]
        )

        gen_total = (
            totals["gen_male"] +
            totals["gen_female"]
        )

        overall_male = (

            totals["sc_male"] +
            totals["bca_male"] +
            totals["bcb_male"] +
            totals["gen_male"]

        )

        overall_female = (

            totals["sc_female"] +
            totals["bca_female"] +
            totals["bcb_female"] +
            totals["gen_female"]

        )

        return {

            "row_type": row_type,

            "class_name": class_name,

            "section_name": "",

            "sc_male": totals["sc_male"],
            "sc_female": totals["sc_female"],
            "sc_total": sc_total,

            "bca_male": totals["bca_male"],
            "bca_female": totals["bca_female"],
            "bca_total": bca_total,

            "bcb_male": totals["bcb_male"],
            "bcb_female": totals["bcb_female"],
            "bcb_total": bcb_total,

            "gen_male": totals["gen_male"],
            "gen_female": totals["gen_female"],
            "gen_total": gen_total,

            "overall_male": overall_male,
            "overall_female": overall_female,
            "overall_total": (
                overall_male +
                overall_female
            ),

        }