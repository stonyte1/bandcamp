from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.urls import reverse_lazy
from .models import Album, Song
from .forms import AlbumForm, SongForm

def home(request):
    return render(request, 'music/home.html')

@login_required
def create_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('music')
        else:
            print(form.errors)
    else:
        form = AlbumForm
    return render(request, 'music/manage_album.html', {'form': form})

@login_required
def create_song(request, pk):
    album = get_object_or_404(Album, pk=pk)

    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            song = form.save(commit=False)
            song.album = album
            song.save()
            return redirect('album_detail', pk=pk)
        else:
            print(form.errors)
    else:
        form = SongForm()

    return render(request, 'music/manage_songs.html', {'form': form})


class AlbumList(generic.ListView):
    model = Album
    template_name = 'music/music.html'
    context_object_name = 'albums'

class AlbumDetailView(generic.DetailView):
    model = Album
    template_name = 'music/album_detail.html'

class AlbumUpdateDeleteView(generic.UpdateView, LoginRequiredMixin):
    model = Album
    template_name = 'music/album_update.html'
    success_url = reverse_lazy('music') 
    form_class = AlbumForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        album = self.get_object()
        context['album'] = album
        return context

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):  
        if 'delete' in request.POST:
            return self.delete(request, *args, **kwargs)
        else:
            return super().post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        album = self.get_object()
        album.delete()
        return redirect(self.success_url)

    def get_object(self, queryset=None):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=self.kwargs['pk'])
        return obj

class SongUpdateView(generic.UpdateView, LoginRequiredMixin):
    model = Song
    template_name = 'music/song_update.html'
    success_url = reverse_lazy('music') 
    form_class = SongForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        song = self.get_object()
        context['song'] = song
        return context

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs): 
        if 'delete' in request.POST:
            return self.delete(request, *args, **kwargs)
        else:
            return super().post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        song = self.get_object()
        song.delete()
        return redirect(self.success_url)

    def get_object(self, queryset=None):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=self.kwargs['pk'])
        return obj

