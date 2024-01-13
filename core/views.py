from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import View
from .forms import PrettyAuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from dough import settings

# Create your views here.

class LoginView(View):
    """
    Login view with a GET and POST method:

    GET method returns the login.html page

    POST method gets the username and password form the form and uses django's built in authenticate function to
    validate the user if the user exists and is active it removes any error messages and sends the user to the home
    screen other wise it renders an error message and keeps the user on the login page
    """
    def post(self, request):
        # Get username and password
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        # django's built in authenticate function returns a user if exists else None
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                # Django's built in login method stores user info in request.session.user
                login(request, user)
                request.session.pop('login_error', None)
                return redirect('home')
            else:
                return HttpResponse("Inactive user.")
        else:
            # Error message to be displayed on screen
            request.session['login_error'] = 'Username or password is incorect.'
            return render(request, 'core/login.html')
    def get(self, request):
        return render(request, "core/login.html")
    

class RegisterView(View):
    """
    Register view with a GET and a POST method:

    GET method renders the register.html screen for the user

    POST method gets the username, first name, last name, email, and password from the form and uses it to create
    a new user with dango's method on the user object create user. It then saves the user and redirects them to
    the login.html screen.
    """
    def post(self, request):
        # Get form data from the register form
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        # Django's built in create user automatically hashes the password and stores the data
        user = User.objects.create_user(username = username, first_name = fname, last_name = lname, email = email, password = password)
        user.save()
        return redirect('login')
        
    def get(self, request):
        return render(request, "core/register.html")
    
class LogoutView(View):
    """
    Logout view with a GET request method:

    GET request uses django's built in logout function that takes in the request and logs out the user from session. It
    then redirects the user to the login.html screen
    """
    def get(self, request):
        # Django's logout function that takes a request and clears all user info
        logout(request)
        return redirect('login')

class Home(View):
    """
    Home view with a GET request method:

    GET request sends the user to the home.html page. Login required checks are handled in the urls.py
    """
    def get(self, request):
        return render(request, 'core/home.html')