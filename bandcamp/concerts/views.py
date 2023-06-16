from django.shortcuts import render
from django.views import generic
from . models import Concert



class ConcertListView(generic.ListView):
    model = Concert
    template_name = "concert_view.html"
    context_object_name = 'concerts'