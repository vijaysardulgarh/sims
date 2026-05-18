from rest_framework.permissions import (
    BasePermission
)


# ==========================================
# CHECK USER PERMISSION
# ==========================================

def has_permission(
    user,
    permission_code
):

    if user.is_superuser:

        return True

    return user.user_roles.filter(

        is_active=True,

        role__role_permissions__permission__code=permission_code,

        role__role_permissions__is_active=True

    ).exists()


# ==========================================
# BASE PERMISSION CLASS
# ==========================================

class HasPermission(
    BasePermission
):

    permission_code = None

    def has_permission(
        self,
        request,
        view
    ):

        if not request.user.is_authenticated:

            return False

        if not self.permission_code:

            return False

        return has_permission(
            request.user,
            self.permission_code
        )


# ==========================================
# STUDENT PERMISSIONS
# ==========================================

class CanViewStudents(
    HasPermission
):

    permission_code = "VIEW_STUDENT"


class CanAddStudent(
    HasPermission
):

    permission_code = "ADD_STUDENT"


class CanEditStudent(
    HasPermission
):

    permission_code = "EDIT_STUDENT"


class CanDeleteStudent(
    HasPermission
):

    permission_code = "DELETE_STUDENT"


# ==========================================
# EXAM PERMISSIONS
# ==========================================

class CanManageExam(
    HasPermission
):

    permission_code = "MANAGE_EXAM"


class CanViewExam(
    HasPermission
):

    permission_code = "VIEW_EXAM"


# ==========================================
# TIMETABLE PERMISSIONS
# ==========================================

class CanManageTimetable(
    HasPermission
):

    permission_code = "MANAGE_TIMETABLE"


class CanViewTimetable(
    HasPermission
):

    permission_code = "VIEW_TIMETABLE"