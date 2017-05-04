# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import View
from django.shortcuts import HttpResponse, Http404, HttpResponseRedirect,HttpResponsePermanentRedirect

from PewaApp.forms import *
from PewaApp.models import *
# Create your views here.


class VendorView(View):

    def get(self, request):
        # < Some logic goes here >
        vendor_form = VendorModelForm()
        vendor_list = Vendor.objects.all()
        return render(request, 'vendor_listing_form.html', {'vendor_form': vendor_form,
                                                    'vendor_list': vendor_list})

    def post(self, request):
        vendor_form = VendorModelForm(request.POST)
        vendor_list = Vendor.objects.all()
        if vendor_form.is_valid():
            vendor_form.save()
            return render(request, 'vendor_listing_form.html', {'vendor_form': vendor_form,
                                                    'vendor_list': vendor_list})
        else:
            return render(request, 'vendor_listing_form.html', {'vendor_form': vendor_form,
                                                       'vendor_list': vendor_list})

    def put(self, request):
        #  < Updating vendor details >
        vendor_form = VendorModelForm(request.POST)
        if vendor_form.is_valid():
            vendor_form.save()
            return render(request, 'vendor_details_form.html', {'vendor_form': vendor_form})
        pass


class ProductView(View):

    def get(self, request):
        product_form = ProductModelForm()
        product_list = Product.objects.all()
        return render(request, 'product_form.html', {'product_form':product_form,
                                                      'product_list':product_list})

    def post(self, request):
        product_form = ProductModelForm(request.POST)
        if product_form.is_valid():
            product_form.save()
        product_list = Product.objects.all()
        return render(request, 'product_form.html', {'product_form': product_form,
                                                         'product_list': product_list})









