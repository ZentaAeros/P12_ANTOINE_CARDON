from rest_framework.permissions import BasePermission, SAFE_METHODS

from .models import MANAGEMENT


class IsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.team == MANAGEMENT and request.method in SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)
