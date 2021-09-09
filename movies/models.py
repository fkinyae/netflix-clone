from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    is_cutomer = models.BooleanField('customer status', default=False)
    is_agent = models.BooleanField('agent status', default=False)

