from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(
        max_length=150, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'  # new

    REQUIRED_FIELDS = ['username', 'password']  # new
