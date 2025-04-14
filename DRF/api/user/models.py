from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import uuid
import rest_framework_simplejwt
from rest_framework_simplejwt.tokens import RefreshToken

GENDER_CHOICES = [
    ('MALE', 'Male'),
    ('FEMALE', 'Female')
]

USER_TYPE_CHOICES = [
    ('CUSTOMER', 'customer'),
    ('RIDER', 'rider'),
    ('STAFF', 'staff')
]

class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=15, unique=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    nationality = models.CharField(max_length=100)
    address = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    user_type = models.CharField(max_length = 10, choices = USER_TYPE_CHOICES, default=USER_TYPE_CHOICES[0][0])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']
    
    
    # def __str__(self):
    #     return f"{self.first_name} {self.last_name}"
    
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
    class Meta:
        db_table = "user"
        