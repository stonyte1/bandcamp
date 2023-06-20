from django.shortcuts import render
from . models import BlogPost
from django.views import generic


class BlogPostListView(generic.ListView):
    model = BlogPost
    template_name = "blog_view.html"
    context_object_name = 'blogpost'