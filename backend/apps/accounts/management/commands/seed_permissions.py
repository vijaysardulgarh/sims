from django.core.management.base import (
    BaseCommand
)

from apps.accounts.permissions.models import (
    Permission
)


# ==========================================
# SEED PERMISSIONS
# ==========================================

class Command(
    BaseCommand
):

    help = (
        "Seed default permissions"
    )

    def handle(
        self,
        *args,
        **kwargs
    ):

        permissions = [

            # ==================================
            # STUDENTS
            # ==================================

            (
                "VIEW_STUDENT",
                "View Student",
                "students"
            ),

            (
                "ADD_STUDENT",
                "Add Student",
                "students"
            ),

            (
                "EDIT_STUDENT",
                "Edit Student",
                "students"
            ),

            (
                "DELETE_STUDENT",
                "Delete Student",
                "students"
            ),

            # ==================================
            # EXAMS
            # ==================================

            (
                "VIEW_EXAM",
                "View Exam",
                "exams"
            ),

            (
                "MANAGE_EXAM",
                "Manage Exam",
                "exams"
            ),

            # ==================================
            # TIMETABLE
            # ==================================

            (
                "VIEW_TIMETABLE",
                "View Timetable",
                "timetable"
            ),

            (
                "MANAGE_TIMETABLE",
                "Manage Timetable",
                "timetable"
            ),
        ]

        created_count = 0

        for code, name, module in permissions:

            _, created = (

                Permission.objects.get_or_create(

                    code=code,

                    defaults={

                        "name": name,

                        "module": module,

                        "is_active": True,
                    }
                )
            )

            if created:

                created_count += 1

        self.stdout.write(

            self.style.SUCCESS(

                f"{created_count} permissions seeded successfully."
            )
        )