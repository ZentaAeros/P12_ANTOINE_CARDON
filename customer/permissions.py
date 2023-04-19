from rest_framework.permissions import BasePermission, SAFE_METHODS

from user.models import SUPPORT, SALES
from .models import Customer


class CustomerPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.user.team == SUPPORT:
            return request.method in SAFE_METHODS
        return request.user.team == SALES

    def has_object_permission(self, request, view, obj):
        if request.method == "DELETE":
            return request.user.team == SALES and obj.status is False
        elif request.user.team == SUPPORT and request.method in SAFE_METHODS:
            return obj in Customer.objects.filter(
                contract__event__support_contact=request.user
            )
        return request.user == obj.sales_contact or obj.status is False
