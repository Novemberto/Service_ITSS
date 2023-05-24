from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('teams/', teams, name='teams'),
    path('service/', service, name='service'),
    path('formation/', formation, name='formation'),
    path('ask_service/', ask_service, name='ask_service'),
    path('demande/', demande, name='demande'),
    
    # path('demande/<int:contact_id>', affichage, name='affichage'),
    
    path('consulter/', consulter, name='consulter'),
    path('voirplus/', voirplus, name='voirplus'),
]