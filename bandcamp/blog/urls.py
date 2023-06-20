from django.urls import path
from . import views


urlpatterns = [
    path('blog/', views.BlogPostListView.as_view(), name='blog'),
]
