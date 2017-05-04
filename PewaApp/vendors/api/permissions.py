from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    message = 'You must be the owner of this object.'
    my_safe_methods = ['GET', ]

    def has_object_permission(self, request, view, obj):
        if request.method in self.my_safe_methods:
            return True
        return obj.created_by == request.user

