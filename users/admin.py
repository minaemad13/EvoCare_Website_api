from django.contrib import admin
# from . import models
from .models import *


class FeedAdmin(admin.ModelAdmin):
    list_display = ('user_id','feedback')


admin.site.register(Feedback, FeedAdmin)
admin.site.register(UserProfile)
admin.site.register(Appointments)

@admin.register(Qr)
class QrAdmin(admin.ModelAdmin):
    list_display = ('user_id','vip', 'qr_code')
    readonly_fields = ['qr_code']
# admin.site.register(Qr,UserAdmin)