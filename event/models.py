from django.db import models
from django.conf import settings

from customer.models import Customer
from contract.models import Contract

# Create your models here.
class Event(models.Model):
    contract = models.OneToOneField(
        to=Contract,
        on_delete=models.CASCADE,
        limit_choices_to={'status': True},
        related_name='event'
    )
    client = models.ForeignKey(to=Customer, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    support_contact = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True
    )
    event_status = models.BooleanField(default=False)
    attendees = models.PositiveBigIntegerField()
    event_date = models.DateTimeField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.client}"
