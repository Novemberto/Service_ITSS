from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='administration'),
    path('site/', our_site, name='site'),
    path('site/logo/', logo_list, name='logo_list'),
    path('site/carousel', carousel_list, name='carousel_list'),
    path('site/partner/', partner_list, name='partner_list'),
]
