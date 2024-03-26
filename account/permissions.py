from rest_framework import permissions
from .models import Student, Teacher
import re
class IsTeacherOrHODOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.is_authenticated:
      
         
            # Check if the user has any of the specified roles
            return user.groups in ['hod']
        return False
