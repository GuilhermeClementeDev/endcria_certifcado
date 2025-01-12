from rest_framework import permissions
from cadet.models import Cadet

class HasRolePermission(permissions.BasePermission):
    required_roles = []

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        try:
            user_roles = Cadet.objects.get(username=request.user.username).roles.all()
            user_role_names = [role.name for role in user_roles]
            return any(role in user_role_names for role in self.required_roles)
        except Cadet.DoesNotExist:
            return False


