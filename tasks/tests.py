from django.test import TestCase
from django.contrib.auth import get_user_model
from tasks.models import Task

class TaskModelTest(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpass'
        )

    def test_create_task(self):
        # Create a task
        task = Task.objects.create(
            user=self.user,
            title='Test Task',
            description='This is a test task.',
            completed=False
        )
        
        # Verify the task was created correctly
        self.assertEqual(task.title, 'Test Task')
        self.assertEqual(task.description, 'This is a test task.')
        self.assertFalse(task.completed)
        self.assertEqual(task.user, self.user)

    def test_task_str(self):
        # Create a task
        task = Task.objects.create(
            user=self.user,
            title='Test Task',
            description='This is a test task.',
            completed=False
        )
        
        # Verify the string representation of the task
        self.assertEqual(str(task), task.title)