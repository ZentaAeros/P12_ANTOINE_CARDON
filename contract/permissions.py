from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.exceptions import PermissionDenied

from user.models import SUPPORT, SALES
from .models import Contract


class ContractPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.user.team == SUPPORT:
            return request.method in SAFE_METHODS
        return request.user.team == SALES

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            if request.user.team == SUPPORT:
                return obj in Contract.objects.filter(
                    event__support_contact=request.user
                )
            return request.user == obj.sales_contact
        elif request.method == "PUT" and obj.status is True:
            raise PermissionDenied("Impossible de mettre à jour un contrat signé.")
        return request.user == obj.sales_contact and obj.status is False
