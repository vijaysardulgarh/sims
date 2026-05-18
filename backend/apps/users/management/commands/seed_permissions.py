from django.core.management.base import (
    BaseCommand
)

from apps.users.models import (
    Role,
    Permission,
    RolePermission
)


class Command(BaseCommand):

    help = (
        "Seed default roles "
        "and permissions"
    )

    def handle(self, *args, **kwargs):

        # =====================================
        # ROLES
        # =====================================

        roles = [

            ("SUPER_ADMIN", "Super Admin"),

            ("CLUSTER_ADMIN", "Cluster Admin"),

            ("SCHOOL_ADMIN", "School Admin"),

            ("PRINCIPAL", "Principal"),

            ("VICE_PRINCIPAL", "Vice Principal"),

            ("TEACHER", "Teacher"),

            ("CLASS_INCHARGE", "Class Incharge"),

            ("EXAM_INCHARGE", "Exam Incharge"),

            ("TIMETABLE_INCHARGE", "Timetable Incharge"),

            ("ACCOUNTANT", "Accountant"),

            ("LIBRARIAN", "Librarian"),

            ("PARENT", "Parent"),

            ("STUDENT", "Student"),
        ]

        role_map = {}

        for code, name in roles:

            role, _ = Role.objects.get_or_create(

                code=code,

                defaults={
                    "name": name
                }
            )

            role_map[code] = role

        self.stdout.write(
            self.style.SUCCESS(
                "Roles seeded successfully"
            )
        )

        # =====================================
        # PERMISSIONS
        # =====================================

        permissions = [

            # STUDENTS

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

            # EXAMS

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

            # TIMETABLE

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

        permission_map = {}

        for code, name, module in permissions:

            permission, _ = (
                Permission.objects.get_or_create(

                    code=code,

                    defaults={

                        "name": name,

                        "module": module,
                    }
                )
            )

            permission_map[code] = permission

        self.stdout.write(
            self.style.SUCCESS(
                "Permissions seeded successfully"
            )
        )

        # =====================================
        # ROLE PERMISSIONS
        # =====================================

        principal_permissions = [

            "VIEW_STUDENT",

            "ADD_STUDENT",

            "EDIT_STUDENT",

            "VIEW_EXAM",

            "MANAGE_EXAM",

            "VIEW_TIMETABLE",
        ]

        principal_role = role_map[
            "PRINCIPAL"
        ]

        for code in principal_permissions:

            RolePermission.objects.get_or_create(

                role=principal_role,

                permission=permission_map[code]
            )

        self.stdout.write(
            self.style.SUCCESS(
                (
                    "Role permissions "
                    "seeded successfully"
                )
            )
        )