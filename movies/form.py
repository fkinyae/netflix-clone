
 
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

class Meta(UserCreationForm.Meta):
    model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.save()
        customer = Customer.objects.create(user=user)
        customer.phone_number = self.cleaned_data.get('phone_number')
        customer.location = self.cleaned_data.get('location')
        customer.save()
        return user




