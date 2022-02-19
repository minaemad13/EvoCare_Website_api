from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(models.Model):
    phone = models.CharField(max_length=13)
    First_Name = models.CharField(max_length=20)
    Last_Name = models.CharField(max_length=20)
    birth = models.CharField(max_length=12, null=False)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=40)
    is_verified = models.BooleanField(null=True)


class Cars(models.Model):
    model = models.CharField(max_length=30)
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


class Appointments(models.Model):
    pass
