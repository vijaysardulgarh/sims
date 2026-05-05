from rest_framework import permissions

# ==========================================
# GLOBAL CUSTOM PERMISSIONS
# Apply these to your ViewSets and APIViews
# ==========================================

class IsAdminRole(permissions.BasePermission):
    """Allows access only to users with the 'admin' role."""
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == 'admin')


class IsPrincipal(permissions.BasePermission):
    """Allows access only to users with the 'principal' role."""
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == 'principal')


class IsAdminOrPrincipal(permissions.BasePermission):
    """
    High-level access: Allows Admin and Principal users.
    Use this for high-level dashboard metrics and staff management.
    """
    def has_permission(self, request, view):
        return bool(
            request.user and 
            request.user.is_authenticated and 
            request.user.role in ['admin', 'principal']
        )


class IsTeacher(permissions.BasePermission):
    """
    Allows access only to users with the 'teacher' role.
    Use this for Class Incharge panels and timetable views.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == 'teacher')


class IsClerk(permissions.BasePermission):
    """
    Allows access only to users with the 'clerk' role.
    Use this for fee collection and document verification endpoints.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == 'clerk')


class IsStudent(permissions.BasePermission):
    """
    Allows access only to users with the 'student' role.
    Use this to restrict students so they can only view their own ledgers and results.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == 'student')

class ReadOnlyPublicAccess(permissions.BasePermission):
    """
    Allows read-only access to anyone (used for the public React website),
    but restricts create/update/delete to Admins only.
    """
    def has_permission(self, request, view):
        # Safe methods are GET, HEAD, OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return True
        # For POST, PUT, DELETE, user must be an Admin
        return bool(request.user and request.user.is_authenticated and request.user.role == 'admin')