from django.shortcuts import render, redirect
from django.views import generic
from django.forms.models import BaseModelForm
from .models import Album
from .forms import AlbumForm
from django.contrib import messages
from django.core.files import File




def home(request):
    return render(request, 'music/home.html')

def album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            title = form.cleaned_data.get('title')
            messages.success(request, f'Album {title} added')
            return redirect('music')
        else:
            # Print form errors to the console
            print(form.errors)
    else:
        form = AlbumForm

    return render(request, 'music/manage_album.html', {'form': form})

class AlbumList(generic.ListView):
    model = Album
    template_name = 'music/music.html'
    context_object_name = 'albums'

class AlbumDetailView(generic.DetailView):
    model = Album
    template_name = 'music/album_detail.html'



