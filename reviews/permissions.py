from rest_framework import permissions

class ReviewPermissionsCustom(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_authenticated

    
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser or obj.critic_id == request.user.id:
            return True