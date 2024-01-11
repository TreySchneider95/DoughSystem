from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path('', LoginView.as_view(), name="login"),
    path('register', RegisterView.as_view(), name="register"),
    path('logout', login_required(LogoutView.as_view()), name='logout'),
    path('home', login_required(Home.as_view()), name="home")
]