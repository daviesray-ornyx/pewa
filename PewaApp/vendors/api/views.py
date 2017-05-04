from __future__ import unicode_literals

from django.db.models import Q

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    RetrieveUpdateDestroyAPIView,
    DestroyAPIView
)


from .permissions import (
    IsOwnerOrReadOnly
)

from .pagination import (
    VendorPageNumberPagination,
    VendorLimitOffsetPagination
)

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly
)

from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
)

from .serializers import (
    VendorDetailSerializer,
    VendorListSerializer,
    VendorCreateSerializer,
    ProductDetailSerializer,
    ProductListSerializer
)

from PewaApp.models import Vendor, Product


class VendorListApiView(ListAPIView):
    serializer_class = VendorListSerializer

    filter_backends = [SearchFilter, OrderingFilter]  #?search= and ordering=
    search_fields = ['name', 'slug', 'email_address']
    pagination_class = VendorPageNumberPagination

    def get_queryset(self, *args, **kwargs):
        queryset = Vendor.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) |
                Q(slug__icontains=query) |
                Q(email_address__icontains=query)
            )
        return queryset
    # This implemented custom search ----


class VendorCreateAPIView(CreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorCreateSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class VendorDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorDetailSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'vendor'
    permission_classes = [IsAuthenticated, ]


class VendorUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorDetailSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'vendor'
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(edited_by=self.request.user) # Here's where you change even the date updated


class VendorDeleteAPIView(RetrieveUpdateDestroyAPIView):
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


