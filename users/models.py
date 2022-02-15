from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models


# Create your models her


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=12, validators=[RegexValidator(regex='^01[0|1|2|5][0-9]{8}$',
                                                                       message='Phone must be start 010, 011, 012, 015 and all number contains 11 digits',
                                                                       code='invalid number')])
    birth = models.DateField(null=False)


class Appointement(models.Model):
    dateandtime = models.CharField()
    User_id = models.ForeignKey(Profile, on_delete=models.CASCADE)

