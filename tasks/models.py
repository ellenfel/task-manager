from django.db import models
from users.models import User

class Task(models.Model):
    # A task belongs to a user
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # The title of the task
    title = models.CharField(max_length=255)
    
    # The description of the task
    description = models.TextField()
    
    # Indicates whether the task is completed or not
    completed = models.BooleanField(default=False)
    
    # The timestamp when the task was created
    created_at = models.DateTimeField(auto_now_add=True)
    
    # The timestamp when the task was last updated
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title