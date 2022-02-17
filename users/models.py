from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models

#<<<<<<< HEAD

# Create your models her


#=======
# Create your models here.


class User(models.Model):
    fullname = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    Email = models.EmailField(max_length=240)


class Cars(models.Model):
    pass


class Appointments(models.Model):
    Date_Time = models.CharField(max_length=30)
    Last_Name = models.CharField(max_length=30)
    First_Name = models.CharField(max_length=30)
    Phone = models.CharField(max_length=30)
    Email = models.CharField(max_length=30)
    User_Id = models.ForeignKey(User, on_delete=models.CASCADE,null=True)






#>>>>>>> 7ba510865f8bb9413ccf27aa48965404b7c63837
