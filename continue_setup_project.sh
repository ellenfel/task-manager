#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Activate virtual environment
source env/bin/activate

# Remove any existing directories that might conflict
rm -rf users/serializers.py tasks/serializers.py

# Create serializers
cat <<EOL > users/serializers.py
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
EOL

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
