from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for the Task model.

    Attributes:
        model (Task): The Task model class.
        fields (list): A list of all fields to be serialized.
    """
    class Meta:
        model = Task
        fields = '__all__'
