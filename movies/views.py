from django.shortcuts import render

from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from .form import CustomerSignUpForm, AgentSignUpForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User

def welcome(request):
    return render(request, 'welcome.html')

def register(request):
    return render(request, 'registration/register.html')




