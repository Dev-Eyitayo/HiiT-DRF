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
    ('STAFF', 'staff'),
    ('ADMIN', 'admin'),
]

class UserManager(BaseUserManager):
    
    def create_user(self,email, password, **extra_fields):
        if not email:
            raise ValueError("Email must be provided")
        if not password:
            raise ValueError("Password must be provided")
        user = self.model(email=self.normalize_email(email), user_type = "ADMIN")
        user.set_password(password)
        user.save()
        return user
    
    def create_user(self, firstname, lastname, email, phone, password=None):
        if not email:
            raise TypeError("Users should have an email")
        if not firstname:
            raise TypeError("Users should have a first name")
        if not lastname:
            raise TypeError("Users should have a last name")
        
        user = self.model(firstname= firstname, lastname=lastname, email = self.normalize_email(email), phone=phone)
        user.set_password(password)
        user.save()
    
        return user
    
    def create_superuser(self, firstname, lastname, email, phone, password=None):
        if password is None:
            raise TypeError("password should not be none")
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.is_verified = True
        user.role = "ADMIN"
        user.save()
        
        return user
class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    email = models.EmailField(max_length=255, unique=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to="profile_picture/", null=True, blank=True)
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
    objects = UserManager()
    
    
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
        