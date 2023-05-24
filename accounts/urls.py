from django.urls import path
from .views import *


urlpatterns = [
    path('', login, name = 'login'),
    path('register/', register, name = 'register'),
    path('mon_compte/', profil, name = 'profil'),
    path('logout/', logout, name = 'logout'),
    
    path('change-password/<uidb64>/<token>/', CompletePasswordReset.as_view(), name='reset_user_password'),
    path('reset-password/', RequestPasswordResetEmail.as_view(), name = 'request_password'),
  
    
]
