from django.urls import path,include
from . import views

urlpatterns = [
       # login/signup &logout
    path('', views.register, name='register'),
    path('customer_register/', views.customer_register.as_view(), name='customer_register'),
    path('employee_register/', views.agent_register.as_view(), name='employee_register'),
]