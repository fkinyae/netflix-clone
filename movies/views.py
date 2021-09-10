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

class customer_register(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'registration/customer_register.html'

def form_valid(self, form):
    user = form.save()
    login(self.request, user)
    return redirect('/')

class agent_register(CreateView):
    model = User
    form_class = AgentSignUpForm
    template_name = 'registration/agent_register.html'

def form_valid(self, form):
    user = form.save()
    login(self.request, user)
    return redirect('/')

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index/')
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'registration/login.html',
                  context={'form': AuthenticationForm()})



