from django.shortcuts import render
from django.contrib.auth import login as login_auth, logout as logout_auth, authenticate
from django.contrib.auth.decorators import login_required
from django.views import View
from .decorators import *
from .forms import *
from customer.models import *
from accounts.models import *

from django.core.mail import send_mail, EmailMessage
import random

from django.core.validators import ValidationError, validate_email
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.template.loader import render_to_string
# from django.utils import account_activation_token
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.tokens import PasswordResetTokenGenerator

from django.contrib import messages
import uuid
# Create your views here.

def profil(request):
    context = {}
    return render(request,'accounts/profil.html',context)


def login(request):
    logos = Logo.objects.filter(is_active = True)
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login_auth(request, user)
            return redirect('home')
    context={'logos': logos}
    return render(request, 'accounts/login.html', context)

def register(request):
    logos = Logo.objects.filter(is_active = True)
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            user.username= email
            user.save()
            
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login_auth(request, user)
            return redirect('login')
        
    context = {'form' : form, 'logos': logos}
    return render(request, 'accounts/register.html', context)



def logout(request):
    logout_auth(request)
    return redirect('home')




class RequestPasswordResetEmail(View):

    
    def get(self, request):
        
        return render(request, 'accounts/request_password.html')
    
    
    def post(self, request):
        
        lower = "abcdefghijklmnopqrstuvwxyz"
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numbers = "0123456789"
        symbols = "!@#$%^&*()."
        string = lower + upper + numbers + symbols
        length = 10

        generate_password = "".join(random.sample(string,length))
         
        email = request.POST['email']
        
        context = {'values': request.POST}
        
        if not validate_email(email):
               
            messages.error(request, 'Svp entrer un mail valide.')
            return render(request, 'accounts/request_password.html', context)
        
        current_site = get_current_site(request)
        
        if user.exists():
        
            email_contents = {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(forces_bytes(user.pk)),
                'token': PasswordResetTokenGenerator().make_token(user),
            }
        
        link = reverse('reset_user_password', kwargs={'uidb64': email_contents['uid'], 'token': email_contents['token']})
        
        email_subject = 'Mot de passe oublier'
        
        reset_url = 'http://'+current_site.domain+link
        
        email = EmailMessage(
            email_subject,
            'Salut', 'faite un click sur le lien suivant pour changer votre mot de passe \n' + reset_url,
            'contact@it-servicegroup.com',
            [email],
            'votre mot de passe courant: '+ generate_password 
        )
        email.send(fail_silently=False)
        
        
        messages.success(request, 'Un mail vous a été envoyez.')
        return render(request, 'accounts/request_password.html', context)




class CompletePasswordReset(View):
    
    def get(self, request, uidb64, token):
        
        return render(request, 'accounts/reset_user_password.html')
    
    def post(self, request, uidb64, token):
        
        return render(request, 'accounts/reset_user_password.html')