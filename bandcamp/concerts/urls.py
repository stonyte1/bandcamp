from django.urls import path
from . import views


urlpatterns = [
    path('concerts/', views.ConcertListView.as_view(), name='concerts'),
]
