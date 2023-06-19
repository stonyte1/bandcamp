from django.urls import path
from . import views

urlpatterns = [
    path('merch/', views.MerchListView.as_view(), name='merch'),
    path('merch/<int:pk>/', views.MerchDetailView.as_view(), name='merch_detail')
]
