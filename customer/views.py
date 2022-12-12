from django.shortcuts import render
from .models import *
from service.models import *
# Create your views here.

def index(request):
    logos = Logo.objects.filter(is_active = True)
    carousels = Carousel.objects.filter(is_active = True)
    typeservice = TypeService.objects.get(is_public = True, name__icontains = "service")
    principals_services = Service.objects.filter(type = typeservice, is_public = True, is_principal = True)
    formations = Formation.objects.filter(is_public = True, is_principal = True)
    services = Service.objects.filter(is_public = True)
    comments = Comments.objects.filter(is_public=True)
    partner = Partner.objects.filter(is_public = True)
    context = {
        'carousels': carousels,
        'logos': logos,
        'principals_services': principals_services,
        'formations': formations,
        'services': services,
        'comments': comments,
        'partner': partner,
    }
    return render(request, 'customer/pages/index.html', context)

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