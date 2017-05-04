from django.conf.urls import url
from PewaApp.api.views import *

urlpatterns = [
    url(r'^vendors/$', VendorListApiView.as_view(), name='vendor_list'),
    url(r'^vendors/create/$', VendorCreateAPIView.as_view(), name='create'),
    url(r'^vendors/(?P<vendor>[\w-]+)/detail/$', VendorDetailAPIView.as_view(), name='detail'),
    url(r'^vendors/(?P<vendor>[\w-]+)/update/$', VendorUpdateAPIView.as_view(), name='update'),
    url(r'^vendors/(?P<vendor>[\w-]+)/delete/$', VendorDeleteAPIView.as_view(), name='delete'),
    url(r'^products/$', ProductListAPIView.as_view(), name='list'),
    url(r'^products/(?P<product>[\w-]+)/$', ProductDetailAPIView.as_view()),

]

#