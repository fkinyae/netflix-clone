from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('login/', views.login_view, name='login'),
    #path('password/', auth_views.PasswordChangeView.as_view()),
    path('password_change/', views.PasswordsChangeView.as_view(), name='password_change'),
]