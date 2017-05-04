from rest_framework.serializers import ModelSerializer

from RestApp.models import Vendor, Product


class VendorCreateSerializer(ModelSerializer):

    class Meta:
        model = Vendor
        fields = [
            'name',
            'phone_number',
            'email_address']


class VendorListSerializer(ModelSerializer):

    class Meta:
        model = Vendor
        fields = ['name', 'slug', 'phone_number', 'email_address']


class VendorDetailSerializer(ModelSerializer):

    class Meta:
        model = Vendor
        fields = ['pk', 'name', 'slug', 'phone_number', 'email_address']
"""
data = {
    'name': 'Douma Construction',
    'phone_number': '0876567656',
    'email_address': 'douma@gmail.com'
}
"""


class ProductListSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ['name', 'slug', 'vendor', 'price']


class ProductDetailSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ['pk', 'name', 'slug', 'vendor', 'price']