from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import uuid
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
    def create_user(self, email, firstname, lastname, password=None, **extra_fields):
        if not email:
            raise TypeError("Users should have an email")
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            firstname=firstname,
            lastname=lastname,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, firstname, lastname, password=None, **extra_fields):
        if password is None:
            raise TypeError("Password should not be none")
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_verified', True)
        extra_fields.setdefault('user_type', 'ADMIN')
        
        return self.create_user(email, firstname, lastname, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    email = models.EmailField(max_length=255, unique=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to="profile_picture/", null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True) 
    phone = models.CharField(max_length=15, unique=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    nationality = models.CharField(max_length=100)
    address = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default=USER_TYPE_CHOICES[0][0])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname', 'lastname', 'phone']

    objects = UserManager()

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    class Meta:
        db_table = "user"
