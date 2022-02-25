
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from pyexpat import model

# Create your models here.


class UserProfile(models.Model):
    phone = models.CharField(max_length=13)
    First_Name = models.CharField(max_length=20)
    Last_Name = models.CharField(max_length=20)
    birth = models.CharField(max_length=12, null=True)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=40)
    is_verified = models.BooleanField(null=True)



class Cars(models.Model):
    model = models.CharField(max_length=30)
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    
class Feedback(models.Model):
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=40,null=True)
    feedback = models.TextField()
    def _str_(self):
        return self.feedback

#it will edit adding packageid
class Appointments(models.Model):
    Date_Time = models.CharField(max_length=30,null=False, unique=True)
    Last_Name = models.CharField(max_length=30,null=False)
    First_Name = models.CharField(max_length=30,null=False)
    Phone = models.CharField(max_length=30,null=False)
    Email = models.CharField(max_length=30,null=False)
    User_Id = models.ForeignKey(UserProfile, on_delete=models.CASCADE,null=True)

#>>>>>>> 7ba510865f8bb9413ccf27aa48965404b7c63837

