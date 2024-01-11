from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class DoughView(View):
    def get(self, request):
        return render(request, 'manageDough/doughs.html')