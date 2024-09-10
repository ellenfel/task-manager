from rest_framework import viewsets
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
