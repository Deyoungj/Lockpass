from django.db import models
from django.contrib.auth.models import AbstractUser
from .custom_manager import CustomUserManager
from django.utils import timezone




class User(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=100)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username']


    def __str__(self):
        return self.email



