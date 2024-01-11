from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path('doughs', login_required(DoughView.as_view()), name="manage_doughs")
]