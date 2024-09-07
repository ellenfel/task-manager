#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Initialize Git repository
#git init task_manager
#cd task_manager

# Create a virtual environment and activate it
python3 -m venv env
source env/bin/activate

# Install necessary packages
pip install django psycopg2-binary djangorestframework

# Commit initial setup
git add .
git commit -m "Initial setup with virtual environment and installed packages"

# Initialize Django project
django-admin startproject task_manager .
git add .
git commit -m "Initialized Django project"




# Configure PostgreSQL database
cat <<EOL >> task_manager/settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'task_manager_db',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
EOL
git add .
git commit -m "Configured PostgreSQL database"

# Create Django apps
python manage.py startapp users
python manage.py startapp tasks
git add .
git commit -m "Created users and tasks apps"

# Define models
cat <<EOL > users/models.py
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
EOL

cat <<EOL > tasks/models.py
from django.db import models
from users.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
EOL
git add .
git commit -m "Defined models for users and tasks"

# Create serializers
mkdir users/serializers.py
cat <<EOL > users/serializers.py
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
EOL

mkdir tasks/serializers.py
cat <<EOL > tasks/serializers.py
from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
EOL
git add .
git commit -m "Created serializers for users and tasks"

# Create views
cat <<EOL > users/views.py
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
EOL

cat <<EOL > tasks/views.py
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
EOL
git add .
git commit -m "Created views for users and tasks"

# Configure URLs
cat <<EOL > task_manager/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet
from tasks.views import TaskViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
EOL
git add .
git commit -m "Configured URLs for users and tasks"

# Run migrations
python manage.py makemigrations
python manage.py migrate
git add .
git commit -m "Ran initial migrations"

echo "Project setup completed successfully!"
