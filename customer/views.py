from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    return render(request, 'customer/pages/index.html')

def about(request):
    return render(request, 'customer/pages/about.html')

def contact(request):
    return render(request, 'customer/pages/contact.html')

def teams(request):
    return render(request, 'customer/pages/teams.html')

def service(request):
    return render(request, 'customer/pages/service.html')

def formation(request):
    return render(request, 'customer/pages/formation.html')