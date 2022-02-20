from django.contrib import admin
# from . import models
from .models import *


class FeedAdmin(admin.ModelAdmin):
    list_display = ('user_id','feedback')


admin.site.register(Feedback, FeedAdmin)
admin.site.register(UserProfile)
admin.site.register(Appointments)



