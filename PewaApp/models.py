# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

from autoslug import AutoSlugField

# Create your models here.

"""Config Models"""


class AuthMethod(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    date_created = models.DateField(auto_now_add=True, null=False, blank=False)
    created_by = models.ForeignKey(User, blank=False, null=False, related_name='+')
    date_edited = models.DateField(auto_now=True, null=False, blank=False)
    edited_by = models.ForeignKey(User, blank=True, null=True, related_name='+')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Authentication method'
        verbose_name_plural = 'Authentication methods'


class GraphicalView(models.Model):
    name = models.CharField(max_length=50, verbose_name='User Status', blank=False, null=False)
    description = models.CharField(max_length=250, verbose_name='User Status', blank=True, null=True)
    date_created = models.DateField(auto_now_add=True, null=False, blank=False)
    created_by = models.ForeignKey(User, blank=False, null=False, related_name='+')
    date_edited = models.DateField(auto_now=True, null=False, blank=False)
    edited_by = models.ForeignKey(User, blank=True, null=True, related_name='+')
    # Pics -- this section will come on later

    def __str__(self):
        return self.name

    def get_full_description(self):
        return self.name + ' ' + self.description

    class Meta:
        verbose_name = 'Graphical view'
        verbose_name_plural = 'Graphical views'


class UserStatus(models.Model):
    name = models.CharField(max_length=50, verbose_name='User Status', blank=False, null=False)
    description = models.CharField(max_length=250, verbose_name='User Status', blank=True, null=True)
    date_created = models.DateField(auto_now_add=True, null=False, blank=False)
    created_by = models.ForeignKey(User, blank=False, null=False, related_name='+')
    date_edited = models.DateField(auto_now=True, null=False, blank=False)
    edited_by = models.ForeignKey(User, blank=True, null=True, related_name='+')

    def __str__(self):
        return self.name

    def get_full_description(self):
        return self.name + ' ' + self.description

    class Meta:
        verbose_name = 'User status'
        verbose_name_plural = 'User status list'


class ProductStatus(models.Model):
    name = models.CharField(max_length=50, verbose_name='User Status', blank=False, null=False)
    description = models.CharField(max_length=250, verbose_name='User Status', blank=True, null=True)
    date_created = models.DateField(auto_now_add=True, null=False, blank=False)
    created_by = models.ForeignKey(User, blank=False, null=False, related_name='+')
    date_edited = models.DateField(auto_now=True, null=False, blank=False)
    edited_by = models.ForeignKey(User, blank=True, null=True, related_name='+')

    def __str__(self):
        return self.name

    def get_full_description(self):
        return self.name + ' ' + self.description

    class Meta:
        verbose_name = 'Product status'
        verbose_name_plural = 'Product status list'


class TransactionStatus(models.Model):
    name = models.CharField(max_length=50, verbose_name='User Status', blank=False, null=False)
    description = models.CharField(max_length=250, verbose_name='User Status', blank=True, null=True)
    graphical_view = models.ForeignKey(GraphicalView, blank=True, null=True, related_name='+')
    date_created = models.DateField(auto_now_add=True, null=False, blank=False)
    created_by = models.ForeignKey(User, blank=False, null=False, related_name='+')
    date_edited = models.DateField(auto_now=True, null=False, blank=False)
    edited_by = models.ForeignKey(User, blank=True, null=True, related_name='+')

    def __str__(self):
        return self.name

    def get_full_description(self):
        return self.name + ' ' + self.description

    class Meta:
        verbose_name = 'Product status'
        verbose_name_plural = 'Product status list'


class NotificationType(models.Model):
    name = models.CharField(max_length=50, verbose_name='User Status', blank=False, null=False)
    # Danger/Warning/Info e.t.c
    description = models.CharField(max_length=250, verbose_name='User Status', blank=True, null=True)
    date_created = models.DateField(auto_now_add=True, null=False, blank=False)
    created_by = models.ForeignKey(User, blank=False, null=False, related_name='+')
    date_edited = models.DateField(auto_now=True, null=False, blank=False)
    edited_by = models.ForeignKey(User, blank=True, null=True, related_name='+')

    def __str__(self):
        return self.name

    def get_full_description(self):
        return self.name + ' ' + self.description

    class Meta:
        verbose_name = 'Notification type'
        verbose_name_plural = 'Notification types'

"""End of config models"""


class Vendor(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, default=1, related_name='+')
    name = models.CharField(max_length=200, verbose_name='Vendor name', null=False, blank=True)
    slug = AutoSlugField(populate_from='name', unique=True, always_update=False, auto_created=True)
    phone_number = models.CharField(max_length=12, verbose_name='Phone number', null=True, blank=True)
    email_address = models.CharField(max_length=200, verbose_name='Email address', null=True, blank=True)
    auth_methods = models.ManyToManyField(AuthMethod, blank=True, related_name='+')
    date_created = models.DateField(auto_now_add=True, null=True, blank=True)
    created_by = models.ForeignKey(User, blank=False, null=True, related_name='+')
    date_edited = models.DateField(auto_now=True, null=True, blank=True)
    edited_by = models.ForeignKey(User, blank=True, null=True, related_name='+')
    user_status = models.ForeignKey(UserStatus, blank=True, null=True, related_name='+')

    def __str__(self):
        return self.name

    def get_full_description(self):
        return self.name + ' ' + self.phone_number + ' ' + self.email_address

    class Meta:
        verbose_name = 'Vendor'
        verbose_name_plural = 'Vendors'
      

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Product name', null=True, blank=True)
    slug = models.SlugField(unique=True)
    vendor = models.ForeignKey(Vendor, verbose_name='Vendor name', null=True, blank=True, related_name='+')
    price = models.DecimalField(max_digits=10, verbose_name='Price', blank=True, default=0.00, decimal_places=2)
    date_created = models.DateField(auto_now_add=True, null=True, blank=True)
    created_by = models.ForeignKey(User, blank=True, null=True, related_name='+')
    date_edited = models.DateField(auto_now=True, null=True, blank=True)
    edited_by = models.ForeignKey(User, blank=True, null=True, related_name='+')
    product_status = models.OneToOneField(ProductStatus, blank=True, null=True, related_name='+')
    #Images will come in later

    def __str__(self):
        return self.name

    def get_full_description(self):
        return self.name + ' ' + str(self.price)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class UserProfile(models.Model):
    user = models.OneToOneField(User, blank=False, null=False)
    friends = models.ManyToManyField('UserProfile', blank=True, related_name='+')
    auth_methods = models.ManyToManyField(AuthMethod, blank=True, related_name='+')
    date_created = models.DateField(auto_now_add=True, null=False, blank=False)
    created_by = models.ForeignKey(User, blank=False, null=False, related_name='+')
    date_edited = models.DateField(auto_now=True, null=False, blank=False)
    edited_by = models.ForeignKey(User, blank=True, null=True, related_name='+')
    user_status = models.ForeignKey(UserStatus, blank=False, null=False, related_name='+')
    wish_list = models.ManyToManyField(Product, blank=True, related_name='+')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'User profile'
        verbose_name_plural = 'User profiles'


class TransactionTracker(models.Model):
    product = models.ForeignKey(Product, blank=False, null=False, related_name='+')
    vendor = models.ForeignKey(Vendor, blank=False, null=False, related_name='+')
    transaction_status = models.ForeignKey(TransactionStatus, blank=False, null=False, related_name='+')
    date_created = models.DateField(auto_now_add=True, null=False, blank=False)
    created_by = models.ForeignKey(User, blank=False, null=False, related_name='+')
    date_edited = models.DateField(auto_now=True, null=False, blank=False)
    edited_by = models.ForeignKey(User, blank=True, null=True, related_name='+')

    def __str__(self):
        return self.product.__str__() + ' ' + self.vendor.__str__() + ' ' + self.transaction_status.__str__()

    class Meta:
        verbose_name = 'Transaction tracker'
        verbose_name_plural = 'Transaction tracker list'


class Transaction(models.Model):
    product = models.ForeignKey(Product, blank=False, null=False, related_name='+')
    #payment_details = models.ForeignKey(Vendor, blank=False, null=False) # To be looked at later
    vendor = models.ForeignKey(Vendor, blank=False, null=False, related_name='+')
    buyer = models.ForeignKey(User, blank=True, null=True, related_name='+')
    recipient = models.ForeignKey(User, blank=False, null=False, related_name='+')
    transaction_tracker = models.ForeignKey(TransactionTracker, blank=False, null=False)
    date_created = models.DateField(auto_now_add=True, null=False, blank=False)
    created_by = models.ForeignKey(User, blank=False, null=False, related_name='+')
    date_edited = models.DateField(auto_now=True, null=False, blank=False)
    edited_by = models.ForeignKey(User, blank=True, null=True, related_name='+')

    def __str__(self):
        return self.product.__str__() + ' ' + self.vendor.__str__()

    class Meta:
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'


class Notification(models.Model):
    sender = models.ManyToManyField(User, blank=False, related_name='+')
    recipient = models.ManyToManyField(User, blank=False, related_name='+')
    notification_type = models.ForeignKey(NotificationType, blank=False, related_name='+')
    message = models.CharField(max_length=250, blank=False, null=False)
    date_created = models.DateField(auto_now_add=True, null=False, blank=False)
    created_by = models.ForeignKey(User, blank=False, null=False, related_name='+')
    date_edited = models.DateField(auto_now=True, null=False, blank=False)
    edited_by = models.ForeignKey(User, blank=True, null=True, related_name='+')

    def __str__(self):
        return self.sender.__str__() + ' ' + self.notification_type.__str__() + ' ' + self.message

    class Meta:
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'
