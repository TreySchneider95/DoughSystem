from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class TestLoginView(TestCase):
    """
    Testing login view
    test checks:
    - login get request
    - login post request
    - login post with not data
    """
    def setUp(self):
        """
        Inital set up for the test model. This set up defines the client the url and
        creates a user to use
        """
        self.client = Client()
        self.url = reverse('login')
        # Using django's built in create user method to create new user
        self.user = User.objects.create_user('tester', 'test@test.com', 'testing1A!')
    
    def test_login_get(self):
        """
        Test for login get method. This test gets the response and check the code and
        the heml template used.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/login.html')

    def test_login_post(self):
        """
        Test for login post method. This test gets the response and checks the code and
        the redirect url when succesfull
        """
        response = self.client.post(self.url, {
            'username': self.user.username,
            'password': 'testing1A!'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

    def test_login_post_no_data(self):
        """
        Test for login post method with no data provided. This test gets the response and
        checks the code.
        """
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 200)


class TestRegisterView(TestCase):
    """
    Test Register view:
    test checks:
    - Register get method
    - Register post method
    """
    def setUp(self):
        """
        Inital set up for the test model. This set up defines the client, the url, and
        builds a dictionary to use for registering a user.
        """
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
        """
        Test for register get method. This test gets the response and checks the code
        returned
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/register.html')

    def test_register_post(self):
        """
        test for register post method. This test gets the response and checks the code,
        checks the user now exists in the temp DB, and checks the redirect.
        """
        response = self.client.post(self.url, self.user)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.get(username = self.user['username']).username, self.user['username'])
        self.assertRedirects(response, reverse('login'))


class TestLogoutView(TestCase):
    """
    Test Logout view:
    test checks:
    - Logout get method
    """
    def setUp(self):
        """
        Inital set up for the test model. This set up defines the client, the url, the
        login url, and creates a user to be used for the testing.
        """
        self.client = Client()
        self.url_login = reverse('login')
        self.url = reverse('logout')
        self.user = User.objects.create_user('tester', 'test@test.com', 'testing1A!')

    def test_logout_get(self):
        """
        Test for logout get method. This test logs in the user created with the login view
        the test to if the username is in the request. Then it gets the response from the
        logout and tests the username is no longer in the request, the code and the url
        redirected to.
        """
        response = self.client.post(self.url_login, {
            'username': self.user.username,
            'password': 'testing1A!'
        })
        self.assertEqual(response.wsgi_request.user.username, self.user.username)
        response = self.client.get(self.url)
        self.assertNotEqual(response.wsgi_request.user.username, self.user.username)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.url_login)


class TestHomeView(TestCase):
    """
    Test Home view:
    test checks:
    - Home get method not logged in
    - Home get method
    """
    def setUp(self):
        """
        Inital set up for the test model. This set up defines the client, the url, the
        redirect url, and creates a user to be used for the testing.
        """
        self.client = Client()
        self.url = reverse('home')
        self.url_redirect = '/?next=%2Fhome'
        self.user = User.objects.create_user('tester', 'tester@testing.com', 'test1A!')

    def test_home_get_not_logged_in(self):
        """
        Test for home get method not logged in. This test gets the response of going to the
        home url when not logged in. It checks the response code is a redirect and the response
        redirect.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.url_redirect)

    def test_home_get_logged_in(self):
        """
        Test for home get method. This test uses the client login method to login a user and
        gets the response it then checks the status code is a render and the tempate it renders
        """
        self.client.login(username=self.user.username, password='test1A!')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/home.html')