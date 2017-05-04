from django.conf.urls import url

from PewaApp.vendors.api.views import *

urlpatterns = [
    url(r'^$', VendorListApiView.as_view(), name='vendor_list'),
    url(r'^create/$', VendorCreateAPIView.as_view(), name='create'),
    url(r'^(?P<vendor>[\w-]+)/detail/$', VendorDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<vendor>[\w-]+)/update/$', VendorUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<vendor>[\w-]+)/delete/$', VendorDeleteAPIView.as_view(), name='delete'),
]
