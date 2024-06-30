from django.test import TestCase
from .models import Task
from django.contrib.auth.models import User

class TaskModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.task = Task.objects.create(
            title='Test Task',
            description='Test Description',
            status='in_progress',
            priority='medium',
            due_date='2024-01-01T00:00:00Z',
            category='Test Category',
            assigned_to=self.user
        )

    def test_task_creation(self):
        self.assertEqual(self.task.title, 'Test Task')

    def test_task_str(self):
        self.assertEqual(str(self.task), 'Test Task')
