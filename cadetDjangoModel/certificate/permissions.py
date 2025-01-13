from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied
from cadet.models import Cadet
from .models import Roles, Permission, Route
#
#class HasRolePermission(permissions.BasePermission):
#    required_roles = []
#
#    def has_permission(self, request, view):
#        if not request.user.is_authenticated:
#            return False
#
#        try:
#            user_roles = Cadet.objects.get(username=request.user.username).roles.all()
#            user_role_names = [role.name for role in user_roles]
#            return any(role in user_role_names for role in self.required_roles)
#        except Cadet.DoesNotExist:
#            return False
#

def has_permission(user_id, role_id, route_title, method):
    """
    Verifica se um usuário com ID e role_id informados tem permissão para realizar uma ação na rota.
    """
    try:
        # Obtém a rota com base no título
        route = Route.objects.get(title=route_title)

        # Obtém a permissão para o papel do usuário na rota
        permission = Permission.objects.get(role_id=role_id, route=route)

        # Mapeia os métodos HTTP para as permissões
        method_to_permission = {
            "GET": permission.can_view,
            "POST": permission.can_add,
            "PUT": permission.can_edit,
            "DELETE": permission.can_delete,
        }

        # Verifica se o método está permitido
        if not method_to_permission.get(method, False):
            raise PermissionDenied("Você não tem permissão para realizar esta ação.")

    except (Route.DoesNotExist, Permission.DoesNotExist):
        raise PermissionDenied("Permissões para esta rota não foram configuradas.")


