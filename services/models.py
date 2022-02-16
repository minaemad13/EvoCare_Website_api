from django.core.validators import FileExtensionValidator
from django.db import models


# Create your models here.

class Services(models.Model):
    sv_name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.sv_name


class ServicesPictures(models.Model):
    options = (
        ('active', 'Active'),
        ('deactivated', 'Deactivated'),
    )

    sv_id = models.ForeignKey(Services, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    alt = models.TextField(null=True)
    image = models.ImageField(upload_to="services_images")
    date_uploaded = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=11, choices=options, default='active')

    class Meta:
        verbose_name = 'Services Picture'
        verbose_name_plural = 'Services Pictures'

    def __str__(self):
        return self.image.name


class ServicesVideos(models.Model):
    options = (
        ('active', 'Active'),
        ('deactivated', 'Deactivated'),
    )

    sv_id = models.ForeignKey(Services, on_delete=models.CASCADE)
    video = models.FileField(upload_to='services_videos', null=True,
                             validators=[
                                 FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    title = models.CharField(max_length=250)
    alt = models.TextField(null=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=11, choices=options, default='active')

    class Meta:
        verbose_name = 'Services Video'
        verbose_name_plural = 'Services Videos'

    def __str__(self):
        return self.video.name


class Packages(models.Model):
    pass
