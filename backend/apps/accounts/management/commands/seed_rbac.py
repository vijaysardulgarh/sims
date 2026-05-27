# apps/accounts/management/commands/seed_rbac.py

from django.core.management.base import (
    BaseCommand
)

from django.db import transaction

from apps.accounts.modules.models import (
    Module
)

from apps.accounts.permissions.models import (
    Permission
)

from apps.accounts.roles.models import (
    Role
)

from apps.accounts.role_permissions.models import (
    RolePermission
)


# ==========================================
# RBAC CONFIG
# ==========================================

RBAC_CONFIG = {

    # ======================================
    # ACADEMICS
    # ======================================

    "academics": {

        "path": None,

        "children": [

            {
                "name": "Sessions",
                "slug": "sessions",
                "path": "/dashboard/sessions",
            },

            {
                "name": "Subjects",
                "slug": "subjects",
                "path": "/dashboard/subjects",
            },

            {
                "name": "Class Subjects",
                "slug": "class-subjects",
                "path": "/dashboard/class-subjects",
            },

            {
                "name": "Teacher Subject Assignments",
                "slug": "teacher-subject-assignments",
                "path": "/dashboard/teacher-subject-assignments",
            },

            {
                "name": "Classes",
                "slug": "classes",
                "path": "/dashboard/classes",
            },

            {
                "name": "Sections",
                "slug": "sections",
                "path": "/dashboard/sections",
            },

            {
                "name": "Streams",
                "slug": "streams",
                "path": "/dashboard/streams",
            },

            {
                "name": "Mediums",
                "slug": "mediums",
                "path": "/dashboard/mediums",
            },

            {
                "name": "Classrooms",
                "slug": "classrooms",
                "path": "/dashboard/classrooms",
            },

            {
                "name": "Timetables",
                "slug": "timetables",
                "path": "/dashboard/timetables",
            },

            {
                "name": "Timetable Slots",
                "slug": "timetable-slots",
                "path": "/dashboard/timetable-slots",
            },

            {
                "name": "Timetable Generator",
                "slug": "timetable-generator",
                "path": "/dashboard/timetable-generator",
            },

            {
                "name": "Timetable Drag Drop",
                "slug": "timetable-drag-drop",
                "path": "/dashboard/timetable-drag-drop",
            },

            {
                "name": "Days",
                "slug": "days",
                "path": "/dashboard/days",
            },

            {
                "name": "Academic Reports",
                "slug": "academic-reports",
                "path": "/dashboard/academic-reports",
            },
        ]
    },

    # ======================================
    # ACCOUNTS
    # ======================================

    "accounts": {

        "path": None,

        "children": [

            {
                "name": "Users",
                "slug": "users",
                "path": "/dashboard/users",
            },

            {
                "name": "Roles",
                "slug": "roles",
                "path": "/dashboard/roles",
            },

            {
                "name": "Permissions",
                "slug": "permissions",
                "path": "/dashboard/permissions",
            },

            {
                "name": "User Roles",
                "slug": "user-roles",
                "path": "/dashboard/user-roles",
            },

            {
                "name": "Role Permissions",
                "slug": "role-permissions",
                "path": "/dashboard/role-permissions",
            },

            {
                "name": "User Permissions",
                "slug": "user-permissions",
                "path": "/dashboard/user-permissions",
            },

            {
                "name": "Modules",
                "slug": "modules",
                "path": "/dashboard/modules",
            },

            {
                "name": "Reports",
                "slug": "account-reports",
                "path": "/dashboard/account-reports",
            },
        ]
    },

    # ======================================
    # ASSOCIATIONS
    # ======================================

    "associations": {

        "path": None,

        "children": [

            {
                "name": "Associations",
                "slug": "associations",
                "path": "/dashboard/associations",
            },

            {
                "name": "Association Roles",
                "slug": "association-roles",
                "path": "/dashboard/association-roles",
            },

            {
                "name": "Association Members",
                "slug": "association-members",
                "path": "/dashboard/association-members",
            },

            {
                "name": "Association Meetings",
                "slug": "association-meetings",
                "path": "/dashboard/association-meetings",
            },

            {
                "name": "Extracurricular Activities",
                "slug": "extracurricular-activities",
                "path": "/dashboard/extracurricular-activities",
            },

            {
                "name": "SMC Members",
                "slug": "smc-members",
                "path": "/dashboard/smc-members",
            },

            {
                "name": "Staff Association Role Assignments",
                "slug": "staff-association-role-assignments",
                "path": "/dashboard/staff-association-role-assignments",
            },

            {
                "name": "Student Association Role Assignments",
                "slug": "student-association-role-assignments",
                "path": "/dashboard/student-association-role-assignments",
            },

            {
                "name": "Reports",
                "slug": "association-reports",
                "path": "/dashboard/association-reports",
            },
        ]
    },

    # ======================================
    # DOCUMENTS
    # ======================================

    "documents": {

        "path": None,

        "children": [

            {
                "name": "Certificates",
                "slug": "certificates",
                "path": "/dashboard/certificates",
            },

            {
                "name": "ID Cards",
                "slug": "id-cards",
                "path": "/dashboard/id-cards",
            },

            {
                "name": "Documents Management",
                "slug": "documents-management",
                "path": "/dashboard/documents-management",
            },
        ]
    },

    # ======================================
    # EXAMS
    # ======================================

    "exams": {

        "path": None,

        "children": [

            {
                "name": "Exam",
                "slug": "exam",
                "path": "/dashboard/exam",
            },

            {
                "name": "Notifications",
                "slug": "notifications",
                "path": "/dashboard/notifications",
            },

            {
                "name": "Online Exams",
                "slug": "online-exams",
                "path": "/dashboard/online-exams",
            },

            {
                "name": "Question Banks",
                "slug": "question-banks",
                "path": "/dashboard/question-banks",
            },

            {
                "name": "Schedules",
                "slug": "schedules",
                "path": "/dashboard/schedules",
            },

            {
                "name": "Reports",
                "slug": "exam-reports",
                "path": "/dashboard/exam-reports",
            },
        ]
    },

    # ======================================
    # FINANCE
    # ======================================

    "finance": {

        "path": None,

        "children": [

            {
                "name": "Fees Payments",
                "slug": "fees-payments",
                "path": "/dashboard/fees-payments",
            },

            {
                "name": "Fees Structure",
                "slug": "fees-structure",
                "path": "/dashboard/fees-structure",
            },

            {
                "name": "Student Fees",
                "slug": "student-fees",
                "path": "/dashboard/student-fees",
            },

            {
                "name": "Reports",
                "slug": "finance-reports",
                "path": "/dashboard/finance-reports",
            },
        ]
    },

    # ======================================
    # LIBRARY
    # ======================================

    "library": {

        "path": None,

        "children": [

            {
                "name": "Books",
                "slug": "books",
                "path": "/dashboard/books",
            },

            {
                "name": "Book Issues",
                "slug": "book-issues",
                "path": "/dashboard/book-issues",
            },

            {
                "name": "Book Categories",
                "slug": "book-categories",
                "path": "/dashboard/book-categories",
            },

            {
                "name": "Accessions",
                "slug": "accessions",
                "path": "/dashboard/accessions",
            },

            {
                "name": "Reports",
                "slug": "library-reports",
                "path": "/dashboard/library-reports",
            },
        ]
    },

    # ======================================
    # SCHOOLS
    # ======================================

    "schools": {

        "path": None,

        "children": [

            {
                "name": "School Settings",
                "slug": "school-settings",
                "path": "/dashboard/school-settings",
            },

            {
                "name": "Branches",
                "slug": "branches",
                "path": "/dashboard/branches",
            },

            {
                "name": "Reports",
                "slug": "school-reports",
                "path": "/dashboard/school-reports",
            },
        ]
    },

    # ======================================
    # CLUSTER
    # ======================================

    "cluster": {

        "path": None,

        "children": [

            {
                "name": "Cluster Schools",
                "slug": "cluster-schools",
                "path": "/dashboard/cluster-schools",
            },

            {
                "name": "Cluster Staff",
                "slug": "cluster-staff",
                "path": "/dashboard/cluster-staff",
            },

            {
                "name": "Cluster Reports",
                "slug": "cluster-reports",
                "path": "/dashboard/cluster-reports",
            },
        ]
    },

    # ======================================
    # STAFF
    # ======================================

    "staff": {

        "path": None,

        "children": [

            {
                "name": "Staff Profiles",
                "slug": "staff-profiles",
                "path": "/dashboard/staff-profiles",
            },

            {
                "name": "Post Types",
                "slug": "post-types",
                "path": "/dashboard/post-types",
            },

            {
                "name": "Sanctioned Posts",
                "slug": "sanctioned-posts",
                "path": "/dashboard/sanctioned-posts",
            },

            {
                "name": "Class Incharge",
                "slug": "class-incharge",
                "path": "/dashboard/class-incharge",
            },

            {
                "name": "Teacher Attendance",
                "slug": "teacher-attendance",
                "path": "/dashboard/teacher-attendance",
            },

            {
                "name": "Reports",
                "slug": "staff-reports",
                "path": "/dashboard/staff-reports",
            },
        ]
    },

    # ======================================
    # STUDENTS
    # ======================================

    "students": {

        "path": None,

        "children": [

            {
                "name": "Student Profiles",
                "slug": "student-profiles",
                "path": "/dashboard/student-profiles",
            },

            {
                "name": "Student Achievements",
                "slug": "student-achievements",
                "path": "/dashboard/student-achievements",
            },

            {
                "name": "Student Achievers",
                "slug": "student-achievers",
                "path": "/dashboard/student-achievers",
            },

            {
                "name": "Student Reports",
                "slug": "student-reports",
                "path": "/dashboard/student-reports",
            },
        ]
    },

    # ======================================
    # TRANSPORT
    # ======================================

    "transport": {

        "path": None,

        "children": [

            {
                "name": "Vehicles",
                "slug": "vehicles",
                "path": "/dashboard/vehicles",
            },

            {
                "name": "Routes",
                "slug": "routes",
                "path": "/dashboard/routes",
            },

            {
                "name": "Drivers",
                "slug": "drivers",
                "path": "/dashboard/drivers",
            },

            {
                "name": "Transport Assignment",
                "slug": "transport-assignment",
                "path": "/dashboard/transport-assignment",
            },

            {
                "name": "Reports",
                "slug": "transport-reports",
                "path": "/dashboard/transport-reports",
            },
        ]
    },

    # ======================================
    # WEBSITE
    # ======================================

    "website": {

        "path": None,

        "children": [

            {
                "name": "Pages",
                "slug": "pages",
                "path": "/dashboard/pages",
            },

            {
                "name": "Banners",
                "slug": "banners",
                "path": "/dashboard/banners",
            },

            {
                "name": "News",
                "slug": "news",
                "path": "/dashboard/news",
            },

            {
                "name": "Gallery",
                "slug": "gallery",
                "path": "/dashboard/gallery",
            },
        ]
    },
}


# ==========================================
# ACTIONS
# ==========================================

ACTIONS = [

    "view",

    "add",

    "edit",

    "delete",

    "import",

    "export",
]


# ==========================================
# DEFAULT ROLES
# ==========================================

DEFAULT_ROLES = [

    {
        "name": "Super Admin",
        "code": "SUPER_ADMIN",
    },

    {
        "name": "Admin",
        "code": "ADMIN",
    },

    {
        "name": "Principal",
        "code": "PRINCIPAL",
    },

    {
        "name": "Cluster",
        "code": "CLUSTER",
    },

    {
        "name": "Clerk",
        "code": "CLERK",
    },

    {
        "name": "Transport",
        "code": "TRANSPORT",
    },

    {
        "name": "Timetable",
        "code": "TIMETABLE",
    },
]


# ==========================================
# COMMAND
# ==========================================

class Command(
    BaseCommand
):

    help = (
        "Seed RBAC system"
    )

    @transaction.atomic
    def handle(
        self,
        *args,
        **options
    ):

        self.stdout.write(

            self.style.WARNING(

                "\nSeeding RBAC...\n"
            )
        )

        roles_map = {}

        for role_data in DEFAULT_ROLES:

            role, _ = Role.objects.get_or_create(

                name=role_data["name"],

                defaults={

                    "code":
                        role_data["code"],

                    "is_system_role":
                        True,
                }
            )

            roles_map[
                role_data["code"]
            ] = role

            self.stdout.write(

                self.style.SUCCESS(

                    f"✓ Role: {role.name}"
                )
            )

        all_permissions = []

        for parent_slug, config in RBAC_CONFIG.items():

            parent_module, _ = (
                Module.objects.get_or_create(

                    name=parent_slug.title(),

                    defaults={

                        "slug":
                            parent_slug,

                        "path":
                            config.get("path"),

                        "is_menu":
                            True,
                    }
                )
            )

            self.stdout.write(

                self.style.SUCCESS(

                    f"✓ Module: "
                    f"{parent_module.name}"
                )
            )

            for action in ACTIONS:

                permission, _ = (
                    Permission.objects.get_or_create(

                        module=parent_module,

                        action=action,
                    )
                )

                all_permissions.append(
                    permission
                )

            for child in config.get(
                "children",
                []
            ):

                child_module, _ = (
                    Module.objects.get_or_create(

                        name=child["name"],

                        defaults={

                            "parent":
                                parent_module,

                            "slug":
                                child["slug"],

                            "path":
                                child["path"],

                            "is_menu":
                                True,
                        }
                    )
                )

                self.stdout.write(

                    self.style.SUCCESS(

                        f"✓ Child Module: "
                        f"{child_module.name}"
                    )
                )

                for action in ACTIONS:

                    permission, _ = (
                        Permission.objects.get_or_create(

                            module=child_module,

                            action=action,
                        )
                    )

                    all_permissions.append(
                        permission
                    )

        super_admin_role = roles_map.get(
            "SUPER_ADMIN"
        )

        if super_admin_role:

            for permission in all_permissions:

                RolePermission.objects.get_or_create(

                    role=super_admin_role,

                    permission=permission,
                )

        admin_role = roles_map.get(
            "ADMIN"
        )

        if admin_role:

            for permission in all_permissions:

                RolePermission.objects.get_or_create(

                    role=admin_role,

                    permission=permission,
                )

        self.stdout.write(

            self.style.SUCCESS(

                "\n✓ Role Permissions Seeded"
            )
        )

        self.stdout.write(

            self.style.SUCCESS(

                "\n✓ RBAC Seeding Complete\n"
            )
        )