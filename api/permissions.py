from rest_framework.permissions import BasePermission


class AuthorDeleteOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user == obj.author:
            return True
        return False
