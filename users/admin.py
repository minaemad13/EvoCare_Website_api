from django.contrib import admin
# from . import models
from .models import *
class FeedAdmin(admin.ModelAdmin):
    list_display = ('user_id','feedback')





admin.site.register(Feedback,FeedAdmin)
admin.site.register(User)


# Register your models here.

from users.models import Appointments

admin.site.register(Appointments)
