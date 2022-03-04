from django.contrib import admin
from . import models

@admin.register(models.ServicesPictures)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('sv_id', 'title', 'alt', 'image', 'date_uploaded', 'status')
    prepopulated_fields = {'image': ('sv_id',), }
    icon_name = 'image'

@admin.register(models.ServicesVideos)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('sv_id', 'title', 'alt', 'video', 'date_uploaded', 'status')
    prepopulated_fields = {'video': ('sv_id',), }
    icon_name = 'movie'

@admin.register(models.Packages)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('sv_id', 'pck_name', 'pck_price', 'status')
    prepopulated_fields = {'pck_name': ('sv_id',), }
    icon_name = 'add_shopping_cart'

# admin.site.register(models.Services)

@admin.register(models.Services)
class AuthorAdmin(admin.ModelAdmin):
    icon_name = 'local_car_wash'
