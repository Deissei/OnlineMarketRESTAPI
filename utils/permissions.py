from rest_framework import permissions


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.username == obj.username:
            return True
        return bool(request.user.username == obj.username)
