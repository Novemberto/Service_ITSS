from django.shortcuts import render, redirect
from .models import *
from service.models import *
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    logos = Logo.objects.filter(is_active = True)
    carousels = Carousel.objects.filter(is_active = True)
    typeservice = TypeService.objects.get(is_public = True, name__icontains = "service")
    principals_services = Service.objects.filter(type = typeservice, is_public = True, is_principal = True)
    formations = Formation.objects.filter(is_public = True, is_principal = True)
    services = Service.objects.filter(type = typeservice, is_public = True)
    comments = Comments.objects.filter(is_public=True)
    partners = Partner.objects.filter(is_public = True)
    context = {
        'carousels': carousels,
        'logos': logos,
        'principals_services': principals_services,
        'formations': formations,
        'services': services,
        'comments': comments,
        'partners': partners,
    }
    return render(request, 'customer/pages/index.html', context)

def about(request):
    logos = Logo.objects.filter(is_active = True)
    context = {'logos': logos}
    return render(request, 'customer/pages/about.html', context)

def contact(request):
    logos = Logo.objects.filter(is_active = True)
    submited =False
    if request.method == 'POST':
            
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.message = message
        
        contact.save()
        return HttpResponseRedirect('?submited=True')
    else:
       
        contact = Contact()
        if 'submited' in request.GET:
            submited = True
    
    context = {'logos': logos, 'submited': submited}
    return render(request, 'customer/pages/contact.html', context)

def teams(request):
    logos = Logo.objects.filter(is_active = True)
    context = {'logos': logos}
    return render(request, 'customer/pages/teams.html', context)

def service(request):
    logos = Logo.objects.filter(is_active = True)
    services = Service.objects.filter(is_public = True)
    context = {
        'logos': logos,
        'services': services,
        }
    return render(request, 'customer/pages/service.html', context)

def formation(request):
    logos = Logo.objects.filter(is_active = True)
    formations = Formation.objects.filter(is_public = True)
    context = {
        'logos': logos,
        'formations': formations
        }
    return render(request, 'customer/pages/formation.html', context)

@login_required(login_url='login')
def ask_service(request):
    logos = Logo.objects.filter(is_active = True)
    context = {'logos': logos}
    return render(request, 'customer/pages/ask_service.html', context)

    
def demande(request):
    logos = Logo.objects.filter(is_active = True)
    results = Contact.objects.all()
    context = {'logos': logos, 'data': results}
    return render(request, 'customer/pages/demande.html', context)

# def affichage(request, contact_id):
#     contact = Contact.objects.get(id=contact_id)
#     contact.affichage()
#     contact.save()
#     return redirect("demande", pk=contact_id)


def consulter(request):
    logos = Logo.objects.filter(is_active = True)
    context = {'logos': logos}
    return render(request, 'customer/pages/consulter.html', context)


def voirplus(request):
    logos = Logo.objects.filter(is_active = True)
    context = {'logos': logos}
    return render(request, 'customer/pages/voirplus.html', context)


