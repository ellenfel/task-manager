from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer class for the User model.

    This serializer is used to convert User model instances into JSON representation and vice versa.

    Attributes:
        model (User): The User model class.
        fields (list): A list of fields to include in the serialized representation. If set to '__all__', all fields will be included.

    """
    class Meta:
        model = User
        fields = '__all__'