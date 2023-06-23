from django.urls import path
from . import views


urlpatterns = [
    path('', views.BlogPostListView.as_view(), name='blog'),
    path('form/', views.create_blog_post, name='blog_post_form'),
    path('<int:pk>/update/', views.BlogPostUpdateDeleteView.as_view(), name='blog_post_update')
]
