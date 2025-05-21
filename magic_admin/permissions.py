# magic_admin/permissions.py
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    Read-only access is allowed for any request that passes other permission checks (e.g., IsAuthenticated).
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request that has passed previous checks,
        # so we'll always allow GET, HEAD or OPTIONS requests at this stage.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the object.
        # Assumes the model instance has an `owner` attribute.
        return obj.owner == request.user