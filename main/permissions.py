from rest_framework.permissions import BasePermission ,SAFE_METHODS

class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        # Allow safe (read-only) methods for authenticated users
        if request.method in SAFE_METHODS:
            return request.user and request.user.is_authenticated
        
        # Only teachers can create/update/delete
        return request.user and request.user.is_authenticated and request.user.role =='TEACHER'
class IsStaffUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_staff)