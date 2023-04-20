"""
URL configuration for epic_events project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from contract.views import ContractList, ContractDetail
from customer.views import CustomerList, CustomerDetail
from event.views import EventList, EventDetail
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("customers/", CustomerList.as_view(), name="client_list"),
    path("customers/<int:pk>/", CustomerDetail.as_view(), name="client_detail"),
    path("contracts/", ContractList.as_view(), name="contract_list"),
    path("contracts/<int:pk>/", ContractDetail.as_view(), name="contract_detail"),
    path("events/", EventList.as_view(), name="event_list"),
    path("events/<int:pk>/", EventDetail.as_view(), name="event_detail"),
]
