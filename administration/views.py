from django.shortcuts import render
from customer.models import *
# Create your views here.

def index(request):
    return render(request, 'administration/pages/index.html')

def our_site(request):
    logo = Logo.objects.count()
    context = {
        'logo': logo
    }
    return render(request, 'administration/pages/site.html', context)

def logo_list(request):
    logos = Logo.objects.all()
    context = {'logos': logos}
    return render(request, 'administration/pages/site/logo_list.html', context)

def logo_form(request):
    context = {}
    return render(request, 'administration/pages/site/logo_form.html', context)

def carousel_list(request):
    carousels = Carousel.objects.all()
    context = {'carousels': carousels}
    return render(request, 'administration/pages/site/carousel_list.html', context)

def carousel_form(request):
    context = {}
    return render(request, 'administration/pages/site/carousel_form.html', context)

def partner_list(request):
    partners = Partner.objects.all()
    context = {'partners': partners}
    return render(request, 'administration/pages/site/partner_list.html', context)

def partner_form(request):
    context = {}
    return render(request, 'administration/pages/site/partner_form.html', context)