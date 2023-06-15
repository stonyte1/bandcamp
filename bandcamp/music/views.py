from django.shortcuts import render
from django.views import generic
from .models import Album


def home(request):
    return render(request, 'music/home.html')

class AlbumList(generic.ListView):
    model = Album
    template_name = 'music/music.html'
    context_object_name = 'albums'


