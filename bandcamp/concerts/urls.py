from django.urls import path
from . import views


urlpatterns = [
    path('concerts/', views.ConcertListView.as_view(), name='concerts'),
    path('concerts/create', views.ConcertCreateView.as_view(), name='create_concerts'),
    path('venue/create/', views.create_venue, name='venue_create')
]
