# Importing the necessary modules and classes
from rest_framework import viewsets  # Provides a set of views for handling CRUD operations
from .models import User  # Importing the User model from the current directory
from .serializers import UserSerializer  # Importing the UserSerializer from the current directory

# Defining a class named UserViewSet that inherits from viewsets.ModelViewSet
class UserViewSet(viewsets.ModelViewSet):
    # Setting the queryset attribute to retrieve all User objects from the database
    queryset = User.objects.all()
    # Setting the serializer_class attribute to use the UserSerializer for serialization and deserialization
    serializer_class = UserSerializer