from django.db import models

class User(models.Model):
    # This field represents the username of the user
    username = models.CharField(max_length=100, unique=True)

    # This field represents the email of the user
    email = models.EmailField(unique=True)

    # This field represents the password of the user
    password = models.CharField(max_length=100)