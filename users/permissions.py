from rest_framework import permissions
from .models import User

class MyCustomPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return (
          request.user.is_authenticated
          and request.user.is_superuser
        )

class EmployeeAndOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj: User):
        return request.user.is_superuser or request.user == obj
            
