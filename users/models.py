from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # This field represents the username of the user
    username = models.CharField(max_length=100, unique=True)

    # This field represents the email of the user
    email = models.EmailField(unique=True)

    # This field represents the password of the user
    password = models.CharField(max_length=100)

    # REQUIRED_FIELDS should include any fields that are required in addition to the USERNAME_FIELD
    REQUIRED_FIELDS = ['email']  # Example: if email is required

    # Specify the USERNAME_FIELD if different from the default 'username'
    USERNAME_FIELD = 'username'  # or 'email' if you use email for authentication