from django.contrib import admin
from .models import EventMetherologic


class EventMetherologicAdmin(admin.ModelAdmin):
    list_filter = [
        'position',
        'where',
        'status'
    ]
    list_display = [
        'position_name',
        'details',
        'where',
        'position',
        'status',
    ]
    list_per_page = 50
    
admin.site.register(EventMetherologic, EventMetherologicAdmin)