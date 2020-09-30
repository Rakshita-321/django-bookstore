from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='michael',
            email='michael@email.com',
            password='test3pass2word1',
        )
        self.assertEqual(user.username, 'michael')
        self.assertEqual(user.email, 'michael@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username='superuser',
            email='superuser@email.com',
            password='test3pass2word1',
        )
        self.assertEqual(user.username, 'superuser')
        self.assertEqual(user.email, 'superuser@email.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)