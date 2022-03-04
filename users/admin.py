from django.contrib import admin
# from . import models
from .models import *


# class FeedAdmin(admin.ModelAdmin):
#     list_display = ('user_id','feedback')
#
#
# admin.site.register(Feedback, FeedAdmin)
# admin.site.register(UserProfile)
# admin.site.register(Appointments)

@admin.register(Appointments)
class AppointmentsAdmin(admin.ModelAdmin):
    icon_name = 'date_range'

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    icon_name = 'account_circle'

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'feedback')
    icon_name = 'message'

@admin.register(Qr)
class QrAdmin(admin.ModelAdmin):
    list_display = ('user_id','vip', 'qr_code')
    readonly_fields = ['qr_code']
    icon_name = 'wifi_tethering'
# admin.site.register(Qr,UserAdmin)
