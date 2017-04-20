# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from RestApp.models import *


# Register your models here.
class VendorAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email_address')
    search_fields = ('name', 'phone_number', 'email_address')


admin.site.register(Vendor, VendorAdmin)
