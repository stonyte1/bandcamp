from django.urls import path
from . import views

urlpatterns = [
    path('', views.MerchListView.as_view(), name='merch'),
    path('<int:pk>/', views.MerchDetailView.as_view(), name='merch_detail'),
    path('form/', views.create_merch, name='merch_form'),
    path('<int:pk>/update', views.MerchUpdateView.as_view(), name='merch_update'),
]
