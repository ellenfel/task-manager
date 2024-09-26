from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from tasks.models import Task

class UserAuthPermissionsTest(TestCase):

    def setUp(self):
        self.client = APIClient()

        # Create two users
        self.user1 = get_user_model().objects.create_user(
            username='user1',
            password='password123'
        )
        self.user2 = get_user_model().objects.create_user(
            username='user2',
            password='password123'
        )

        # Log in user1
        self.client.login(username='user1', password='password123')

        # Create a task for user1
        self.task = Task.objects.create(
            user=self.user1,
            title='User1 Task',
            description='Task description for user1',
            completed=False
        )

    def test_authenticated_user_can_access_own_tasks(self):
        """Ensure that authenticated users can access their own tasks."""
        response = self.client.get(reverse('task-detail', args=[self.task.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.task.title)

    def test_authenticated_user_cannot_access_other_users_tasks(self):
        """Ensure authenticated users cannot access tasks owned by other users."""
        # Log in user2
        self.client.logout()
        self.client.login(username='user2', password='password123')

        # Try to access task created by user1
        response = self.client.get(reverse('task-detail', args=[self.task.id]))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_unauthenticated_user_cannot_access_any_tasks(self):
        """Ensure unauthenticated users cannot access tasks."""
        self.client.logout()
        response = self.client.get(reverse('task-detail', args=[self.task.id]))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_user_can_create_task(self):
        """Ensure authenticated users can create tasks."""
        data = {
            'title': 'New Task',
            'description': 'New task description',
            'completed': False
        }
        response = self.client.post(reverse('task-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'New Task')

    def test_unauthenticated_user_cannot_create_task(self):
        """Ensure unauthenticated users cannot create tasks."""
        self.client.logout()
        data = {
            'title': 'Task created by unauthenticated user',
            'description': 'This should not be allowed.',
            'completed': False
        }
        response = self.client.post(reverse('task-list'), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_user_can_update_own_task(self):
        """Ensure users can update their own tasks."""
        data = {
            'title': 'Updated Task Title',
            'description': 'Updated task description',
            'completed': True
        }
        response = self.client.put(reverse('task-detail', args=[self.task.id]), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, 'Updated Task Title')
        self.assertTrue(self.task.completed)

    def test_authenticated_user_cannot_update_other_users_tasks(self):
        """Ensure users cannot update tasks that belong to other users."""
        # Log in user2
        self.client.logout()
        self.client.login(username='user2', password='password123')

        # Try to update user1's task
        data = {
            'title': 'Attempt to update',
            'description': 'User2 attempting to update User1 task',
            'completed': True
        }
        response = self.client.put(reverse('task-detail', args=[self.task.id]), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_can_delete_own_task(self):
        """Ensure users can delete their own tasks."""
        response = self.client.delete(reverse('task-detail', args=[self.task.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_authenticated_user_cannot_delete_other_users_tasks(self):
        """Ensure users cannot delete tasks that belong to other users."""
        # Log in user2
        self.client.logout()
        self.client.login(username='user2', password='password123')

        # Try to delete user1's task
        response = self.client.delete(reverse('task-detail', args=[self.task.id]))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
