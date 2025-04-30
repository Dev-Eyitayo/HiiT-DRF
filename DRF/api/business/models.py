from django.db import models
import uuid
# from user.models import CustomUser
from django.contrib.auth import get_user_model


User = get_user_model()
class Business(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to = "businessLogo/")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner")
    type = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=255)
    phone = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    
    def __str__(self):
        return f"{self.name} by {self.owner.firstname} {self.owner.lastname}"