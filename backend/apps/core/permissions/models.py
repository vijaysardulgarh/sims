from django.db import models

from apps.core.roles.models import Role


class Permission(models.Model):

    module = models.CharField(
        max_length=100
    )

    action = models.CharField(
        max_length=100
    )

    code = models.CharField(
        max_length=150,
        unique=True
    )

    def __str__(self):

        return self.code


class RolePermission(models.Model):

    role = models.ForeignKey(
        Role,
        on_delete=models.CASCADE,
        related_name="permissions"
    )

    permission = models.ForeignKey(
        Permission,
        on_delete=models.CASCADE
    )