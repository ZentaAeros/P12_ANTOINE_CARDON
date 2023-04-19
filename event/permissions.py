from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.exceptions import PermissionDenied

from user.models import SUPPORT, SALES


class EventPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.user.team == SUPPORT:
            return request.method in ["GET", "PUT"]
        return request.user.team == SALES

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return (
                request.user == obj.support_contact
                or request.user == obj.contract.sales_contact
            )
        else:
            if obj.event_status is True:
                raise PermissionDenied(
                    "Impossible de mettre à jour un événement terminé."
                )
            if request.user.team == SUPPORT:
                return request.user == obj.support_contact
            return request.user == obj.contract.sales_contact
