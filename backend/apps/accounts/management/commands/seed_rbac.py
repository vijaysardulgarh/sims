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
                "name": "Subjects",
                "slug": "subjects",
                "path": "/dashboard/academics/subjects",
            },

             {
                "name": "Sessions",
                "slug": "sessions",
                "path": "/dashboard/academics/sessions",
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
                "name": "System Modules",
                "slug": "system-modules",
                "path": "/dashboard/accounts/system-modules",
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
                "name": "Committees",
                "slug": "committees",
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
                "name": "Association Role Assignments",
                "slug": "association-role-assignments",
                "path": "/dashboard/associations/association-role-assignments",
            },

        ]
    },


    # ======================================
    # COMMUNICATIONS
    # ======================================

    "communications": {

        "path": None,

        "children": [

            {
                "name": "Circulars",
                "slug": "circulars",
                "path": "/dashboard/communications/circulars",
            },

            {
                "name": "Events",
                "slug": "events",
                "path": "/dashboard/communications/events",
            },

            {
                "name": "Notices",
                "slug": "notices",
                "path": "/dashboard/communications/notices",
            },

            {
                "name": "News",
                "slug": "news",
                "path": "/dashboard/communications/news",
            },

            {
                "name": "Faqs",
                "slug": "faqs",
                "path": "/dashboard/communications/faqs",
            },

            {
                "name": "communication-templates",
                "slug": "communication-templates",
                "path": "/dashboard/communications/communication-templates",
            },

            {
                "name": "Communication Categories",
                "slug": "communication-categories",
                "path": "/dashboard/communications/communication-categories",
            },

            {
                "name": "Notifications",
                "slug": "notifications",
                "path": "/dashboard/communications/notifications",
            },
        ]
    },

    # ======================================
    # COMPLIANCE
    # ======================================

    "compliance": {

        "path": None,

        "children": [

            {
                "name": "Affiliations",
                "slug": "affiliations",
                "path": "/dashboard/compliance/affiliations",
            },

            {
                "name": "Certificates",
                "slug": "certificates",
                "path": "/dashboard/compliance/certificates",
            },

            {
                "name": "Compliance Documents",
                "slug": "compliance-documents",
                "path": "/dashboard/compliance/compliance-documents",
            },

            {
                "name": "Inspections",
                "slug": "inspections",
                "path": "/dashboard/compliance/inspections",
            },

            {
                "name": "Mandatory Public Disclosures",
                "slug": "mandatory-public-disclosures",
                "path": "/dashboard/compliance/mandatory-public-disclosures",
            },

            {
                "name": "policies",
                "slug": "policies",
                "path": "/dashboard/compliance/policies",
            },

            {
                "name": "Recognitions",
                "slug": "recognitions",
                "path": "/dashboard/compliance/recognitions",
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

        ]
    },


    "infrastructure": {

        "path": None,
        

        "children": [

            {
                "name": "Buildings",
                "slug": "buildings",
                "path": "/dashboard/infrastructure/buildings",
            },

            {
                "name": "Classrooms",
                "slug": "classrooms",
                "path": "/dashboard/infrastructure/classrooms",
            },


            {
                "name": "Floors",
                "slug": "floors",
                "path": "/dashboard/infrastructure/floors",
            },

            {
                "name": "Rooms",
                "slug": "rooms",
                "path": "/dashboard/infrastructure/rooms",
            },  

            {
                "name": "laboratories",
                "slug": "laboratories",
                "path": "/dashboard/infrastructure/laboratories",
            },

            {
                "name": "auditoriums",
                "slug": "auditoriums",
                "path": "/dashboard/infrastructure/auditoriums",
            },

            {
                "name": "facilities",
                "slug": "facilities",
                "path": "/dashboard/infrastructure/facilities",
            },

            {
                "name": "Hostel-Facilities",
                "slug": "hostel-facilities",    
                "path": "/dashboard/infrastructure/hostel-facilities",
            },

            {
                "name": "inventories",
                "slug": "inventories",
                "path": "/dashboard/infrastructure/inventories",
            },

            {
                "name": "libraries",
                "slug": "libraries",
                "path": "/dashboard/infrastructure/libraries",
            },

            {
                "name": "Playgrounds",
                "slug": "playgrounds",
                "path": "/dashboard/infrastructure/playgrounds",
            },

            {
                "name": "Sports-Facilities",
                "slug": "sports-facilities",
                "path": "/dashboard/infrastructure/sports-facilities",
            },

            {
                "name": "Transport-Facilities",
                "slug": "transport-facilities",
                "path": "/dashboard/infrastructure/transport-facilities",
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
                "name": "About School",
                "slug": "about-school",
                "path": "/dashboard/schools/about-school",
            },

            {
                "name": "School Records",
                "slug": "school-records",
                "path": "/dashboard/schools/schools",
            },

            {
                "name": "Branches",
                "slug": "branches",
                "path": "/dashboard/schools/branches",
            },

            {
                "name": "Galleries",
                "slug": "galleries",
                "path": "/dashboard/schools/galleries",
            },

            {
                "name": "Principals",
                "slug": "principals",
                "path": "/dashboard/schools/principals",
            },

            {
                "name": "School-Settings",
                "slug": "school-settings",
                "path": "/dashboard/schools/school-settings",
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
                "slug": "clusters-schools",
                "path": "/dashboard/cluster/clusters",
            },

            {
                "name": "Cluster Staff",
                "slug": "cluster-staff",
                "path": "/dashboard/cluster/cluster-staff",
            },

        ]
    },

    # ======================================
    # STAFF
    # ======================================

    "human-resources": {

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

        ]
    },

    # ======================================
    # STUDENTS
    # ======================================

    "students": {

        "path": None,

        "children": [

            {
                "name": "Student List",
                "slug": "student-list",
                "path": "/dashboard/students/list",
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
                "name": "Student Strength",
                "slug": "student-strength",
                "path": "/dashboard/students/reports/student-strength",
            },

        ]
    },

    # ======================================
    # TIMETABLES
    # ======================================

    "timetables": {

        "path": None,

        "children": [

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
                "name": "Timetable Record",
                "slug": "timetable-record",
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

        ]
    },

    # ======================================
    # WEBSITE
    # ======================================

    "compliance": {

        "path": None,

        "children": [

            {
                "name": "affiliations",
                "slug": "affiliations",
                "path": "/dashboard/compliance/affiliations",
            },

            {
                "name": "certificates",
                "slug": "certificates",
                "path": "/dashboard/compliance/certificates",
            },

            {
                "name": "compliance-documents",
                "slug": "compliance-documents",
                "path": "/dashboard/compliance/compliance-documents",
            },

            {
                "name": "inspections",
                "slug": "inspections",
                "path": "/dashboard/compliance/inspections",
            },
            {
                "name": "mandatory-public-disclosures",
                "slug": "mandatory-public-disclosures",
                "path": "/dashboard/compliance/mandatory-public-disclosures",
            },

            {
                "name": "policies",
                "slug": "policies",
                "path": "/dashboard/compliance/policies",
            },

            {
                "name": "recognitions",
                "slug": "recognitions",
                "path": "/dashboard/compliance/recognitions",
            },
        ]
    },


    # ======================================
    # REPORTS
    # ======================================

    "reports": {

        "path": None,

        "children": [

            {
                "name": "Student Reports",
                "slug": "student-reports",
                "path": "/dashboard/reports/student-reports",
            },

            {
                "name": "Staff Reports",
                "slug": "staff-reports",
                "path": "/dashboard/reports/staff-reports",
            },

            {
                "name": "Academic Reports",
                "slug": "academic-reports",
                "path": "/dashboard/reports/academic-reports",
            },

            {
                "name": "Finance Reports",
                "slug": "finance-reports",
                "path": "/dashboard/reports/finance-reports",
            },

            {
                "name": "Library Reports",
                "slug": "library-reports",
                "path": "/dashboard/reports/library-reports",
            },

            {
                "name": "Transport Reports",
                "slug": "transport-reports",
                "path": "/dashboard/reports/transport-reports",
            },

            {
                "name": "Association Reports",
                "slug": "association-reports",
                "path": "/dashboard/reports/association-reports",
            },

            {
                "name": "School Reports",
                "slug": "school-reports",
                "path": "/dashboard/reports/school-reports",
            },

            {
                "name": "Cluster Reports",
                "slug": "cluster-reports",
                "path": "/dashboard/reports/cluster-reports",
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

                    slug=parent_slug,

                    defaults={

                        "name": (
                            config.get("name")
                            or parent_slug.replace("-", " ").title()
                        ),

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

                child_module, created = Module.objects.get_or_create(

                    slug=child["slug"],

                    defaults={

                        "name": child["name"],

                        "parent": parent_module,

                        "path": child["path"],

                        "is_menu": True,
                    }
                )

                if not created:

                    if child_module.id == parent_module.id:
                        raise ValueError(
                            f"Module '{child_module.slug}' "
                            f"cannot be its own parent."
                        )

                    child_module.parent = parent_module

                    child_module.name = child["name"]

                    child_module.path = child["path"]

                    child_module.is_menu = True

                    child_module.save()

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