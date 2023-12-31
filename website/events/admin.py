from django.contrib import admin
from .models import Venue
from .models import Event

# Register your models here.

# admin.site.register(Event)
# admin.site.register(Venue)

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display=("name", "address", "phone_number")
    ordering=("name",)
    search_fields=("name", "address")

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields=(("name", "venue"), "event_date", "description", "manager", "attendees")
    list_display=("name", "event_date", "venue")
    ordering=("-event_date", "name")
    list_filter=("event_date", "venue")
    search_fields=("name",)