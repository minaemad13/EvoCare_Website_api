from django.contrib import admin
from . import models

@admin.register(models.ServicesPictures)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('sv_id', 'title', 'alt', 'image', 'date_uploaded', 'status')
    prepopulated_fields = {'image': ('sv_id',), }

@admin.register(models.ServicesVideos)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('sv_id', 'title', 'alt', 'video', 'date_uploaded', 'status')
    prepopulated_fields = {'video': ('sv_id',), }


@admin.register(models.Packages)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('sv_id', 'pck_name', 'pck_price', 'status')
    prepopulated_fields = {'pck_name': ('sv_id',), }

admin.site.register(models.Services)