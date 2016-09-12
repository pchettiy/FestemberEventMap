from django.contrib import admin
from .models import Stall

class StallAdmin(admin.ModelAdmin):
    list_display = ["stallId","stallName","stallDescription","stallLocation"]
    search_fields = ["stallId","stallName","stallDescription","stallLocation"]
    
    class Meta:
        model = Stall
        
admin.site.register(Stall , StallAdmin)
