from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class BaseTest(TestCase):
    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.user = {
            'email': 'testemail@gmail.com',
            'username': 'username',
            'password': 'password',
            'last_name': 'namee',
            'first_name': 'name'
        }
        self.user_short_password = {
            'email': 'testemail@gmail.com',
            'username': 'username',
            'password': 'pass',
            'last_name': 'namee',
            'first_name': 'name'
        }

        self.user_invalid_email = {

            'email': 'testemail',
            'username': 'username',
            'password': 'password',
            'last_name': 'namee',
            'first_name': 'name'
        }
        return super().setUp()


class RegisterTest(BaseTest):

   def test_can_register_user(self):
        response = self.client.post(
            self.register_url, self.user)
        self.assertEqual(response.status_code, 201)

   def test_cant_register_user_withshortpassword(self):
        response = self.client.post(
            self.register_url, self.user_short_password)
        self.assertEqual(response.status_code, 400)

   def test_cant_register_user_with_invalid_email(self):
        response = self.client.post(
            self.register_url, self.user_invalid_email)
        self.assertEqual(response.status_code, 400)

   def test_cant_register_user_with_taken_email(self):
        self.client.post(self.register_url, self.user)
        response = self.client.post(
            self.register_url, self.user)
        self.assertEqual(response.status_code, 400)


class LoginTest(BaseTest):

    def test_login_success(self):
        self.client.post(self.register_url, self.user)
        response = self.client.post(
            self.login_url, self.user)
        self.assertEqual(response.status_code, 200)

    def test_cantlogin_with_no_username(self):
        response = self.client.post(
            self.login_url, {'password': 'passwped', 'username': ''})
        self.assertEqual(response.status_code, 401)

    def test_cantlogin_with_no_password(self):
        response = self.client.post(
            self.login_url, {'username': 'passwped', 'password': ''})
        self.assertEqual(response.status_code, 401)
