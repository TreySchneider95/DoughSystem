from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class TestLoginView(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('login')
        self.user = User.objects.create_user('tester', 'test@test.com', 'testing1A!')
    
    def test_login_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/login.html')

    def test_login_post(self):
        response = self.client.post(self.url, {
            'username': self.user.username,
            'password': 'testing1A!'
        })
        self.assertEqual(response.status_code, 302)

    def test_login_post_no_data(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 200)


class TestRegisterView(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('register')
        self.user = {
            'username': 'tester',
            'password': 'testing1A!',
            'fname': 'test',
            'lname': 'er',
            'email': 'tester@test.com'
        }
    
    def test_register_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/register.html')

    def test_register_post(self):
        response = self.client.post(self.url, self.user)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.get(username = self.user['username']).username, self.user['username'])


class TestLogoutView(TestCase):
    def setUp(self):
        self.client = Client()
        self.url_login = reverse('login')
        self.url = reverse('logout')
        self.user = User.objects.create_user('tester', 'test@test.com', 'testing1A!')

    def test_logout_get(self):
        response = self.client.post(self.url_login, {
            'username': self.user.username,
            'password': 'testing1A!'
        })
        self.assertEqual(response.wsgi_request.user.username, self.user.username)
        response = self.client.get(self.url)
        self.assertNotEqual(response.wsgi_request.user.username, self.user.username)


class TestHomeView(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('home')
        self.url_redirect = reverse('login')
        self.user = User.objects.create_user('tester', 'tester@testing.com', 'test1A!')

    def test_home_get_not_logged_in(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)

    def test_home_get_logged_in(self):
        self.client.login(username=self.user.username, password='test1A!')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/home.html')