from __future__ import unicode_literals

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
)

from .serializers import (
    VendorDetailSerializer,
    VendorListSerializer,
    VendorCreateSerializer,
    ProductDetailSerializer,
    ProductListSerializer
)

from RestApp.models import Vendor, Product


class VendorListApiView(ListAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorListSerializer


class VendorCreateAPIView(CreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorCreateSerializer


class VendorDetailAPIView(RetrieveAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorDetailSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'vendor'


class VendorUpdateAPIView(UpdateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorDetailSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'vendor'


class VendorDeleteAPIView(DestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorDetailSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'vendor'


""" Product Section """


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'product'


