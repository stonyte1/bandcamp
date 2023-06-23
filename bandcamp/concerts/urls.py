from django.urls import path
from . import views


urlpatterns = [
    path('', views.ConcertListView.as_view(), name='concerts'),
    path('create/', views.ConcertCreateView.as_view(), name='create_concerts'),
    path('<int:pk>/update/', views.ConcertUpdateDeleteView.as_view(), name='concert_update'),
]
