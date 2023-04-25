from rest_framework import permissions
from rest_framework.permissions import IsAdminUser, SAFE_METHODS
from rest_framework.response import Response
from rest_framework import status


class AuthorCreateorDeleteOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user


class IsAdminUserOrReadOnly(IsAdminUser):
    def has_permission(self, request, view):
        is_admin = super(
            IsAdminUserOrReadOnly,
            self).has_permission(request, view)
        if is_admin:
            return request.method in SAFE_METHODS or is_admin
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
