from django.forms import ModelForm

from RestApp.models import *

# Vendor form


class VendorModelForm(ModelForm):

    class Meta:
        model = Vendor
        fields = ['name', 'phone_number', 'email_address', ]


class ProductModelForm(ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'vendor', 'price']


