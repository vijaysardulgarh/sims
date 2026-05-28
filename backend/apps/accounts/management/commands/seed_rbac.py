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
                "path": "/dashboard/academics/subjects",
            },

            {
                "name": "Class Subjects",
                "slug": "class-subjects",
                "path": "/dashboard/academics/class-subjects",
            },

            {
                "name": "Teacher Subject Assignments",
                "slug": "teacher-subject-assignments",
                "path": "/dashboard/academics/teacher-subject-assignments",
            },

            {
                "name": "Classes",
                "slug": "classes",
                "path": "/dashboard/academics/classes",
            },

            {
                "name": "Sections",
                "slug": "sections",
                "path": "/dashboard/academics/sections",
            },

            {
                "name": "Streams",
                "slug": "streams",
                "path": "/dashboard/academics/streams",
            },

            {
                "name": "Mediums",
                "slug": "mediums",
                "path": "/dashboard/academics/mediums",
            },

            {
                "name": "Classrooms",
                "slug": "classrooms",
                "path": "/dashboard/academics/classrooms",
            },

            {
                "name": "Timetables",
                "slug": "timetables",
                "path": "/dashboard/academics/timetables",
            },

            {
                "name": "Timetable Slots",
                "slug": "timetable-slots",
                "path": "/dashboard/academics/timetable-slots",
            },

            {
                "name": "Timetable Generator",
                "slug": "timetable-generator",
                "path": "/dashboard/academics/timetable-generator",
            },

            {
                "name": "Timetable Drag Drop",
                "slug": "timetable-drag-drop",
                "path": "/dashboard/academics/timetable-drag-drop",
            },

            {
                "name": "Days",
                "slug": "days",
                "path": "/dashboard/academics/days",
            },

            {
                "name": "Academic Reports",
                "slug": "academic-reports",
                "path": "/dashboard/academics/academic-reports",
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
                "path": "/dashboard/accounts/users",
            },

            {
                "name": "Roles",
                "slug": "roles",
                "path": "/dashboard/accounts/roles",
            },

            {
                "name": "Permissions",
                "slug": "permissions",
                "path": "/dashboard/accounts/permissions",
            },

            {
                "name": "User Roles",
                "slug": "user-roles",
                "path": "/dashboard/accounts/user-roles",
            },

            {
                "name": "Role Permissions",
                "slug": "role-permissions",
                "path": "/dashboard/accounts/role-permissions",
            },

            {
                "name": "User Permissions",
                "slug": "user-permissions",
                "path": "/dashboard/accounts/user-permissions",
            },

            {
                "name": "Modules",
                "slug": "modules",
                "path": "/dashboard/accounts/modules",
            },

            {
                "name": "Reports",
                "slug": "account-reports",
                "path": "/dashboard/accounts/account-reports",
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
                "path": "/dashboard/associations/associations",
            },

            {
                "name": "Association Roles",
                "slug": "association-roles",
                "path": "/dashboard/associations/association-roles",
            },

            {
                "name": "Association Members",
                "slug": "association-members",
                "path": "/dashboard/associations/association-members",
            },

            {
                "name": "Association Meetings",
                "slug": "association-meetings",
                "path": "/dashboard/associations/association-meetings",
            },

            {
                "name": "Extracurricular Activities",
                "slug": "extracurricular-activities",
                "path": "/dashboard/associations/extracurricular-activities",
            },

            {
                "name": "SMC Members",
                "slug": "smc-members",
                "path": "/dashboard/associations/smc-members",
            },

            {
                "name": "Staff Association Role Assignments",
                "slug": "staff-association-role-assignments",
                "path": "/dashboard/associations/staff-association-role-assignments",
            },

            {
                "name": "Student Association Role Assignments",
                "slug": "student-association-role-assignments",
                "path": "/dashboard/associations/student-association-role-assignments",
            },

            {
                "name": "Reports",
                "slug": "association-reports",
                "path": "/dashboard/associations/association-reports",
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
                "path": "/dashboard/exams/exam",
            },

            {
                "name": "Notifications",
                "slug": "notifications",
                "path": "/dashboard/exams/notifications",
            },

            {
                "name": "Online Exams",
                "slug": "online-exams",
                "path": "/dashboard/exams/online-exams",
            },

            {
                "name": "Question Banks",
                "slug": "question-banks",
                "path": "/dashboard/exams/question-banks",
            },

            {
                "name": "Schedules",
                "slug": "schedules",
                "path": "/dashboard/exams/schedules",
            },

            {
                "name": "Reports",
                "slug": "exam-reports",
                "path": "/dashboard/exams/exam-reports",
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
                "path": "/dashboard/finance/fees-payments",
            },

            {
                "name": "Fees Structure",
                "slug": "fees-structure",
                "path": "/dashboard/finance/fees-structure",
            },

            {
                "name": "Student Fees",
                "slug": "student-fees",
                "path": "/dashboard/finance/student-fees",
            },

            {
                "name": "Reports",
                "slug": "finance-reports",
                "path": "/dashboard/finance/finance-reports",
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
                "path": "/dashboard/library/books",
            },

            {
                "name": "Book Issues",
                "slug": "book-issues",
                "path": "/dashboard/library/book-issues",
            },

            {
                "name": "Book Categories",
                "slug": "book-categories",
                "path": "/dashboard/library/book-categories",
            },

            {
                "name": "Accessions",
                "slug": "accessions",
                "path": "/dashboard/library/accessions",
            },

            {
                "name": "Reports",
                "slug": "library-reports",
                "path": "/dashboard/library/library-reports",
            },
        ]
    },

    # ======================================
    # SCHOOLS
    # ======================================

    "schools": {
        "name": "School",
        "slug": "school-dashbaord",
        "path": "/dashboard/schools",

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
                "path": "/dashboard/cluster/cluster-schools",
            },

            {
                "name": "Cluster Staff",
                "slug": "cluster-staff",
                "path": "/dashboard/cluster/cluster-staff",
            },

            {
                "name": "Cluster Reports",
                "slug": "cluster-reports",
                "path": "/dashboard/cluster/cluster-reports",
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
                "path": "/dashboard/staff/staff-profiles",
            },

            {
                "name": "Post Types",
                "slug": "post-types",
                "path": "/dashboard/staff/post-types",
            },

            {
                "name": "Sanctioned Posts",
                "slug": "sanctioned-posts",
                "path": "/dashboard/staff/sanctioned-posts",
            },

            {
                "name": "Class Incharge",
                "slug": "class-incharge",
                "path": "/dashboard/staff/class-incharge",
            },

            {
                "name": "Teacher Attendance",
                "slug": "teacher-attendance",
                "path": "/dashboard/staff/teacher-attendance",
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
                "path": "/dashboard/students/student-profiles",
            },

            {
                "name": "Student Achievements",
                "slug": "student-achievements",
                "path": "/dashboard/students/student-achievements",
            },

            {
                "name": "Student Achievers",
                "slug": "student-achievers",
                "path": "/dashboard/students/student-achievers",
            },

            {
                "name": "Student Reports",
                "slug": "student-reports",
                "path": "/dashboard/students/student-reports",
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
                "path": "/dashboard/transport/vehicles",
            },

            {
                "name": "Routes",
                "slug": "routes",
                "path": "/dashboard/transport/routes",
            },

            {
                "name": "Drivers",
                "slug": "drivers",
                "path": "/dashboard/transport/drivers",
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
                "path": "/dashboard/website/pages",
            },

            {
                "name": "Banners",
                "slug": "banners",
                "path": "/dashboard/website/banners",
            },

            {
                "name": "News",
                "slug": "news",
                "path": "/dashboard/website/news",
            },

            {
                "name": "Gallery",
                "slug": "gallery",
                "path": "/dashboard/website/gallery",
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