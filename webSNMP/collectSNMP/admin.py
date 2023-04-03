from django.contrib import admin

# Register your models here.

from .models import Device, SNMPInfo

admin.site.register(Device)
admin.site.register(SNMPInfo)
