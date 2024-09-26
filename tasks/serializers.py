from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for the Task model.

    Attributes:
        model (Task): The Task model class.
        fields (list): A list of all fields to be serialized.
    """

    # The user field is read-only and will be set to the current user
    class Meta:
        model = Task
        fields = ['id', 'user', 'title', 'description', 'completed', 'created_at', 'updated_at']
        read_only_fields = ['user', 'created_at', 'updated_at']


    # Override the create method to set the user field to the current user
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)