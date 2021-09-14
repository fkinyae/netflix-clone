from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    is_customer = models.BooleanField('customer status', default=False)
    is_agent = models.BooleanField('agent status', default=False)
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    phone_number = models.CharField(max_length = 10,blank =True)
    Address =models.CharField(max_length=100)

class Agent(models. Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    phone_number = models.CharField(max_length = 10,blank =True)
    Address =models.CharField(max_length=100)


