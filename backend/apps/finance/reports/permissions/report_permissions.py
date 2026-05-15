from rest_framework.permissions import BasePermission


class CanViewFinanceReports(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated