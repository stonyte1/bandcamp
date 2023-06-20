from django import forms
from .models import Album, Song

class AlbumForm(forms.ModelForm):
    
    class Meta:
        model = Album
        fields = ['title', 'cover', 'release_date', 'summary', 'realese_type']
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'})
        }

class SongForm(forms.ModelForm):
    
    class Meta:
        model = Song
        fields = ['title', 'audio', 'duration', 'album']


 