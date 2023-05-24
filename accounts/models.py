from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
# Create your models here.

class User(AbstractUser):
    phone = PhoneNumberField(unique = True, verbose_name="Téléphone", null = True, blank = True)
    email = models.EmailField(unique = True, null = True, blank = True)

    class Meta(AbstractUser.Meta):
       swappable = 'AUTH_USER_MODEL'


# class Profile(models.Model):
   
#     email = models.EmailField(unique = True, null = True, blank = True)
#     forget_password_token = models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)
   
#     def __str__(self):
#         return self.email.username

