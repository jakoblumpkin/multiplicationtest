from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Test(models.Model):
    username=models.OneToOneField(User, on_delete=models.CASCADE)
    question1=models.CharField(max_length=7, default='incorrect')
    question2 = models.CharField(max_length=7, default='incorrect')
    question3 = models.CharField(max_length=7, default='incorrect')
    question4 = models.CharField(max_length=7, default='incorrect')



