from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.exceptions import ValidationError
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from user.models import SALES, SUPPORT
from .models import Customer
from user.permissions import IsManager
from .permissions import CustomerPermissions
from .serializers import CustomerSerializer


class CustomerList(ListCreateAPIView):
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated, IsManager | CustomerPermissions]
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ["^first_name", "^last_name", "^email", "^company_name"]
    filterset_fields = ["status"]

    def get_queryset(self):
        if self.request.user.team == SUPPORT:
            return Customer.objects.filter(
                contract__event__support_contact=self.request.user
            ).distinct()
        elif self.request.user.team == SALES:
            prospects = Customer.objects.filter(status=False)
            own_clients = Customer.objects.filter(sales_contact=self.request.user)
            return prospects | own_clients
        return Customer.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            if serializer.validated_data["status"] is True:
                serializer.validated_data["sales_contact"] = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class CustomerDetail(RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    http_method_names = ["get", "put", "delete", "options"]
    permission_classes = [IsAuthenticated, IsManager | CustomerPermissions]
    serializer_class = CustomerSerializer

    def update(self, request, *args, **kwargs):
        client = self.get_object()
        serializer = CustomerSerializer(data=request.data, instance=client)
        if serializer.is_valid(raise_exception=True):
            if client.status is True and serializer.validated_data["status"] is False:
                raise ValidationError(
                    {"detail": "Impossible de modifier le statut du client converti."}
                )
            elif serializer.validated_data["status"] is True:
                serializer.validated_data["sales_contact"] = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
