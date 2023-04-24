from django.contrib import admin
from .models import Contract

# Register your models here.

class ContractAdmin(admin.ModelAdmin):
    list_display = ('client', 'sales_contact', 'status', 'amount', 'payment_due')

admin.site.register(Contract, ContractAdmin)
