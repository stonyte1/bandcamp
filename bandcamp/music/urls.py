from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.AlbumList.as_view(), name='music'),
    path('<int:pk>/', views.AlbumDetailView.as_view(), name='album_detail'),
    path('form/', views.create_album, name='album_form'),
    path('<int:pk>/song/', views.create_song, name='song_form'),
    path('<int:pk>/update/', views.AlbumUpdateDeleteView.as_view(), name='album_update'),
    path('song/<int:pk>', views.SongUpdateView.as_view(), name='song_update')
]
