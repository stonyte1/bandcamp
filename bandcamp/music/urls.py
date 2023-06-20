from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('music/', views.AlbumList.as_view(), name='music'),
    path('music/<int:pk>/', views.AlbumDetailView.as_view(), name='album_detail'),
    path('music/form/', views.album, name='album_form'),
    path('music/<int:pk>/song/', views.song, name='song_form'),
    path('music/<int:pk>/update/', views.AlbumUpdateDeleteView.as_view(), name='album_update'),
    path('music/song/<int:pk>', views.SongUpdateDeleteView.as_view(), name='song_update')
]
