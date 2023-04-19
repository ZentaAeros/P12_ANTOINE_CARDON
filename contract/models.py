from django.db import models
from django.conf import settings

from customer.models import Customer

# Create your models here.
class Contract(models.Model):
    client = models.ForeignKey(to=Customer, on_delete=models.CASCADE)
    sales_contact = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    status = models.BooleanField(default=False)
    amount = models.FloatField()
    payment_due = models.DateField()

    def __str__(self):
        return f"{self.client}"
