from django import forms
from .models import Merch


class MerchForm(forms.ModelForm):
    
    class Meta:
        model = Merch
        fields = ('name', 'category', 'album', 'price', 'quantity', 'picture', 'description')
        
