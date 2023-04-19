from django.db import models
from django.conf import settings

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    company_name = models.CharField(max_length=250, blank=True, null=True)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    sales_contact = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True
    )
    status = models.BooleanField(default=False, verbose_name="Converted")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
