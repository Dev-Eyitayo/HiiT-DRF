from rest_framework.permissions import BasePermission

class IsFemaleUser(BasePermission):
    
    def has_permissions(self, request, view):
        user = request.user
        # Check if the user's gender is female
        if user.gender != "female":
            return False  
        return True 
