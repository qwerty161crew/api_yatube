from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework import permissions


class AuthorDeleteOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user == obj.author:
            return True
        return False
    
# class CreateGroupAdminOnly(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.user.is_staff():
#             return True
#         return False

