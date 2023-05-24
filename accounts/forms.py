from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields=('email', 'phone', 'password1','password2')
        
        
        
        
        
# class ResetForm(forms.ModelForm):
#     class Meta:
       
#         model = Reset
#         fields = ['email']
      
# class ConfirmForm(forms.ModelForm):
  
#     class Meta:
#         model = Confirm
#         fields = ('current', 'password', 'confirm_password')