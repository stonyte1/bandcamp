from django.urls import path
from . import views


urlpatterns = [
    path('blog/', views.BlogPostListView.as_view(), name='blog'),
    path('blog/form/', views.blog_post, name='blog_post_form'),
    path('blog/<int:pk>/update/', views.BlogPostUpdateDeleteView.as_view(), name='blog_post_update')
]
