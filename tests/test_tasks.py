from django.test import TestCase
from django.core.exceptions import ValidationError
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

    def test_create_task_with_missing_title(self):
        with self.assertRaises(ValidationError):
            task = Task(user=self.user, description='Test description')
            task.full_clean()  # This will raise a ValidationError

    def test_create_task_with_invalid_completed_status(self):
        with self.assertRaises(ValidationError):
            task = Task(user=self.user, title='Test Task', description='Test description', completed='not_a_boolean')
            task.full_clean()  # This will raise a ValidationError

    def test_create_task_with_empty_title(self):
        with self.assertRaises(ValidationError):
            task = Task(user=self.user, title='', description='Test description')
            task.full_clean()  # This will raise a ValidationError

    def test_create_task_with_excessively_long_title(self):
        with self.assertRaises(ValidationError):
            task = Task(user=self.user, title='a' * 256, description='Test description')
            task.full_clean()  # This will raise a ValidationError

    def test_task_creation_timestamps(self):
        task = Task.objects.create(user=self.user, title='Test Task', description='Test description')
        self.assertIsNotNone(task.created_at)
        self.assertIsNotNone(task.updated_at)

    def test_task_update_timestamps(self):
        task = Task.objects.create(user=self.user, title='Test Task', description='Test description')
        original_updated_at = task.updated_at
        task.title = 'Updated Task'
        task.save()
        self.assertNotEqual(task.updated_at, original_updated_at)

    def test_task_deletion(self):
        task = Task.objects.create(user=self.user, title='Test Task', description='Test description')
        task_id = task.id
        task.delete()
        with self.assertRaises(Task.DoesNotExist):
            Task.objects.get(id=task_id)

    def test_create_task_with_max_title_length(self):
        task = Task.objects.create(user=self.user, title='a' * 255, description='Test description')
        task.full_clean()  # Should not raise ValidationError

    #$ python manage.py test tests -v 2

    def test_create_task_with_max_description_length(self):
        task = Task.objects.create(user=self.user, title='Test Task', description='a' * 1000)
        task.full_clean()


"""

    def test_create_task_with_excessively_long_description(self):
        with self.assertRaises(ValidationError):
            task = Task(user=self.user, title='Test Task', description='a' * 1001)
            task.full_clean()


    def test_create_task_with_empty_description(self):
        task = Task.objects.create(user=self.user, title='Test Task', description='')
        task.full_clean()   # Should not raise ValidationError

    def test_create_task_with_null_description(self):
        task = Task.objects.create(user=self.user, title='Test Task')
        task.full_clean()

    def test_create_task_with_null_completed_status(self):
        task = Task.objects.create(user=self.user, title='Test Task', description='Test description')
        task.full_clean()

    def test_create_task_with_null_user(self):
        with self.assertRaises(ValidationError):
            task = Task(title='Test Task', description='Test description')
            task.full_clean()

    def test_create_task_with_invalid_user(self):
        with self.assertRaises(ValueError):
            task = Task(user='invalid_user', title='Test Task', description='Test description')
            task.full_clean()
"""