from django.contrib import admin
from .models import Event

# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ['eventName','eventTime','eventLocation','eventStatus']
    search_fields = ['eventName','eventLocation','eventStatus']
    
    class Meta:
        model = Event
        
admin.site.register(Event, EventAdmin)