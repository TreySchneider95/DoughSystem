from django.test import SimpleTestCase
from django.urls import reverse, resolve
from core.views import LoginView, RegisterView, LogoutView, Home


class testUrls(SimpleTestCase):
    """
    Tests that each url is resolved by getting the reverse of each url and asserting the resolve of that reverse
    is equal to the view.
    """
    def test_login_is_resolved(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func.__name__, LoginView.as_view().__name__)

    def test_register_is_resolved(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func.__name__, RegisterView.as_view().__name__)

    def test_logout_is_resolved(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func.__name__, LogoutView.as_view().__name__)

    def test_home_is_resolved(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func.__name__, Home.as_view().__name__)