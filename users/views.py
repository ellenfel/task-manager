# Importing the necessary modules and classes
from rest_framework import viewsets  # Provides a set of views for handling CRUD operations
from .models import User  # Importing the User model from the current directory
from .serializers import UserSerializer  # Importing the UserSerializer from the current directory
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

# Defining a class named UserViewSet that inherits from viewsets.ModelViewSet
class UserViewSet(viewsets.ModelViewSet):
    # Setting the queryset attribute to retrieve all User objects from the database
    queryset = User.objects.all()
    # Setting the serializer_class attribute to use the UserSerializer for serialization and deserialization
    serializer_class = UserSerializer

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        refresh = RefreshToken.for_user(user)
        return Response({
            'token': str(refresh.access_token),
        })
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
    user = User.objects.create_user(username=username, email=email, password=password)
    return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_current_user(request):
    return Response({
        'username': request.user.username,
        'email': request.user.email,
    })