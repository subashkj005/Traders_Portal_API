from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be a staff')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be a superuser.')

        return self.create_user(email, password, **extra_fields)
    
    
class Users(AbstractBaseUser, PermissionsMixin):
    REGISTRATION_CHOICES = [
        ('email', 'Email'),
        ('google', 'Google'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, null=False)
    uid = models.CharField(max_length=255, blank=True, null=True, editable=False)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255, blank=True)
    registration_method = models.CharField(max_length=10, choices=REGISTRATION_CHOICES, default='email')
    created_at = models.DateTimeField(auto_now_add=True)
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    
    def __str__(self) -> str:
        return self.email

# # class Company(models.Model):
# #     id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
# #     company_name = models.CharField(max_length=255, null=False,blank=False)
# #     symbol = models.CharField(max_length=255, null=True, blank=True)
# #     scripcode = models.CharField(max_length=255, null=True, blank=True)



