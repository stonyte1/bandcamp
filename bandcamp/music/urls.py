from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('music/', views.AlbumList.as_view(), name='music'),
    path('music/<int:pk>', views.AlbumDetailView.as_view(), name='album_detail'),
]
