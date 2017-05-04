from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination
)


class VendorPageNumberPagination(PageNumberPagination):
    page_size = 10


class VendorLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100