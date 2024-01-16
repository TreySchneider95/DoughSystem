from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path('doughs', login_required(DoughView.as_view()), name="manage_doughs"),
    path('make_purchases', login_required(MakePurchases.as_view()), name="make_purchases"),
    path('manage_raw_inventory', login_required((ManageRawInventory.as_view())), name='manage_raw_inventory')
]