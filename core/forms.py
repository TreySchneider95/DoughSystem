from django.contrib.auth.forms import AuthenticationForm
from django import forms

class PrettyAuthenticationForm(AuthenticationForm):
    class Meta:
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control form-control-lg'})
        }