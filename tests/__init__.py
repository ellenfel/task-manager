# Ensure the test module is in the same directory
from .test_tasks import TaskModelTest

# Use TaskModelTest to avoid unused import warning
__all__ = ['TaskModelTest']