from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from pyexpat import model

import qrcode
import random
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
from django.db.models.signals import pre_delete, post_save
from django.dispatch import receiver
# Create your models here.
from services.models import Packages


class UserProfile(models.Model):
    phone = models.CharField(max_length=13, unique=True)
    First_Name = models.CharField(max_length=20)
    Last_Name = models.CharField(max_length=20)
    birth = models.CharField(max_length=40, null=True)
    email = models.EmailField(max_length=30, unique=True)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=40)

    def __str__(self):
        name=self.First_Name + " "+ self.Last_Name
        return (name )


class Cars(models.Model):
    model = models.CharField(max_length=30)
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


class Feedback(models.Model):
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=40, null=True)
    feedback = models.TextField()

    def _str_(self):
        return self.feedback


# it will edit adding packageid
class Appointments(models.Model):
    Date_Time = models.CharField(max_length=30, null=False, unique=True)
    Last_Name = models.CharField(max_length=30, null=False)
    First_Name = models.CharField(max_length=30, null=False)
    Phone = models.CharField(max_length=30, null=False)
    Email = models.CharField(max_length=30, null=False)
    User_Id = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=False)
    package_id = models.ForeignKey(Packages, on_delete=models.CASCADE, null=False)
    package_price = models.FloatField(null=False)

    def __str__(self):
        return self.Date_Time


# >>>>>>> 7ba510865f8bb9413ccf27aa48965404b7c63837


class Qr(models.Model):
    user_id = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    vip = models.BooleanField(default=False)
    qr_code = models.ImageField(upload_to='qr_codes', blank=True)

    class Meta:
        verbose_name = ('QR code')

    def __str__(self):
        return str(self.user_id.First_Name)

    def create_qr(self):
        if self.vip:
            print(self.user_id.id)
            url = f"http://127.0.0.1:8000/admin/users/userprofile/{self.user_id.id}"
            qrcode_img = qrcode.make(
                url)
            canvas = Image.new('RGB', (450, 400), 'white')
            canvas.paste(qrcode_img)
            fname = f'qr_code-{self.user_id}{random.randint(1000, 9999)}.png'
            buffer = BytesIO()
            canvas.save(buffer, 'PNG')
            self.qr_code.save(fname, File(buffer), save=False)
            canvas.close()

    def save(self, *args, **kwargs):
        self.create_qr()
        super(Qr, self).save(*args, **kwargs)


@receiver(pre_delete, sender=Qr)
def qr_delete(sender, instance, **kwargs):
    instance.qr_code.delete(False)

# @receiver(post_save, sender=Qr)
# def update_history_field(sender, instance, **kwargs):
#  if instance.vip == False:
#     instance.qr_code.delete(False)
