from django.urls import path
from . import views

urlpatterns = [
    path('merch/', views.MerchListView.as_view(), name='merch'),
    path('merch/<int:pk>/', views.MerchDetailView.as_view(), name='merch_detail'),
    path('merch/form/', views.merch, name='merch_form'),
    path('merch/<int:pk>/update', views.MerchUpdateView.as_view(), name='merch_update'),
]
