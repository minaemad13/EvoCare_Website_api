
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from pyexpat import model


# Create your models here.
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None
    phone = models.CharField(max_length=13)
    First_Name = models.CharField(max_length=20)
    Last_Name = models.CharField(max_length=20)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class UserProfile(models.Model):
    phone = models.CharField(max_length=13)
    First_Name = models.CharField(max_length=20)
    Last_Name = models.CharField(max_length=20)
    birth = models.CharField(max_length=10, null=True)
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
class Appointments(models.Model):
    Date_Time = models.CharField(max_length=30)
    Last_Name = models.CharField(max_length=30)
    First_Name = models.CharField(max_length=30)
    Phone = models.CharField(max_length=30)
    Email = models.CharField(max_length=30)
    User_Id = models.ForeignKey(UserProfile, on_delete=models.CASCADE,null=True)






#>>>>>>> 7ba510865f8bb9413ccf27aa48965404b7c63837

