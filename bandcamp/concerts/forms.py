from django import forms
from .models import Concert, ConcertVenue

class ConcertForm(forms.ModelForm):
    
    class Meta:
        model = Concert
        fields = ['city_name', 'venue_name', 'date', 'ticket_status', 'link', 'visible']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }
