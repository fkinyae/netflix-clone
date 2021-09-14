from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm 
from django.urls import reverse_lazy

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
    
class    PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('welcome')
    
