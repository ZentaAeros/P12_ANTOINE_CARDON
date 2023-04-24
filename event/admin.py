from django.contrib import admin

from .models import Event

# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ('contract', 'support_contact', 'event_status', 'attendees', 'event_date')

admin.site.register(Event, EventAdmin)
