from django.test import TestCase
from .models import Bug

# Create your tests here.


class BugTest(TestCase):
    """
    Define tests for bug model
    """

    def test_str(self):
        test_name = Bug(summary='Test Summary')
        self.assertEqual(str(test_name), 'Test Summary')
