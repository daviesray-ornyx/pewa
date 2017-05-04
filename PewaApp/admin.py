# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from PewaApp.models import *


# Register your models here.
class VendorAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email_address')
    search_fields = ('name', 'phone_number', 'email_address')

admin.site.register(Vendor, VendorAdmin)


class AuthMethodAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'date_created', 'created_by', 'edited_by', 'date_edited',)
    search_fields = ('name', 'description', 'date_created', 'created_by', 'edited_by', 'date_edited',)

admin.site.register(AuthMethod, AuthMethodAdmin)


class GraphicalViewAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'date_created', 'created_by', 'edited_by', 'date_edited',)
    search_fields = ('name', 'description', 'date_created', 'created_by', 'edited_by', 'date_edited',)

admin.site.register(GraphicalView, GraphicalViewAdmin)


class UserStatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'date_created', 'created_by', 'edited_by', 'date_edited',)
    search_fields = ('name', 'description', 'date_created', 'created_by', 'edited_by', 'date_edited',)

admin.site.register(UserStatus, UserStatusAdmin)


class ProductStatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'date_created', 'created_by', 'edited_by', 'date_edited',)
    search_fields = ('name', 'description', 'date_created', 'created_by', 'edited_by', 'date_edited',)

admin.site.register(ProductStatus, ProductStatusAdmin)


class TransactionStatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'graphical_view', 'date_created', 'created_by', 'edited_by', 'date_edited',)
    search_fields = ('name', 'description', 'date_created', 'created_by', 'edited_by', 'date_edited',)

admin.site.register(TransactionStatus, TransactionStatusAdmin)


class NotificationTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'date_created', 'created_by', 'edited_by', 'date_edited',)
    search_fields = ('name', 'description', 'date_created', 'created_by', 'edited_by', 'date_edited',)

admin.site.register(NotificationType, NotificationTypeAdmin)
