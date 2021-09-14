from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login, logout 
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm
from django.urls import reverse_lazy
from .models import User
from django.contrib import messages
from django.views.generic import CreateView
from django.shortcuts import redirect, render




def welcome(request):
    return render(request, 'welcome.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username,password)
        
        user = authenticate(request, password=password, username=username)
        if user is None:
            context = {"error": "Invalid username or password"}
            return render(request, "accounts/login.html",context)
        login(request,user)
        return redirect('welcome')

    return render(request, "accounts/login.html")

def logout_view(request):
    logout(request)
    return redirect('login')

class    PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('welcome')
    
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


    
