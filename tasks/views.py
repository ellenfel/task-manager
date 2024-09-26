from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    """
    A view set for managing tasks.

    This view set provides CRUD (Create, Retrieve, Update, Delete) operations for tasks.

    Attributes:
        queryset (QuerySet): The queryset of all tasks.
        serializer_class (Serializer): The serializer class used for task serialization.

    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    # Override the get_queryset method to only return tasks owned by the current user
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)