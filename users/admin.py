from django.contrib import admin

# Register your models here.

from users.models import Appointments

admin.site.register(Appointments)
