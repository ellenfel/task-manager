from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Add extra fields here if needed, but do NOT redefine username, email, or password
    pass