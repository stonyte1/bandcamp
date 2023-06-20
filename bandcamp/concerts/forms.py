from django import forms
from .models import Concert, ConcertVenue

class ConcertForm(forms.ModelForm):
    
    class Meta:
        model = Concert
        fields = ['city', 'venue', 'date', 'ticket_status', 'link', 'visible']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }


class ConcertVenueForm(forms.ModelForm):
    
    class Meta:
        model = ConcertVenue
        fields = ['city', 'name']
