
 
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User, Customer, Agent


 
class CustomerSignUpForm(UserCreationForm):
 
   first_name = forms.CharField(required=True)
   last_name = forms.CharField(required=True)
   email = forms.EmailField(required=True)
   phone_number = forms.CharField(required=False)
   location = forms.CharField(required=True)


