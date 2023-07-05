from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models



class CustomUserManager(BaseUserManager):
    def create_superuser(self, email: str = None, password=None, **extr_fields):
        extr_fields.setdefault('is_staff', True)
        extr_fields.setdefault('is_superuser', True)
        extr_fields.setdefault('is_active', True)

        if extr_fields.get('is_active') is not True:
            raise ValueError("is_active must be set to true")
        
        if extr_fields.get('is_superuser') is not True:
            raise ValueError("is_superuser must be set to true")

        if not email:
            raise ValueError("Email is required")


    def create_user(self, email, password, **extra_fileds):
        
        if not email:
            raise ValueError("Email Required")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fileds)

        user.set_password(password)
        user.save()
        return user


class User(AbstractUser):
    pass