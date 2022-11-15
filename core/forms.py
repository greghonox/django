from django import forms
from .models import EventMetherologic


class EventMetherologicForms(forms.ModelForm):
    
    class Meta:
        model = EventMetherologic
        fields = [
            'position_name',
            'details',
            'position',
            'status',
        ]