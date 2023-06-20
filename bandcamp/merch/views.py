from django.shortcuts import render
from django.views import generic
from .models import Merch


class MerchListView(generic.ListView):
    model = Merch
    template_name = "merch/merch.html"
    context_object_name = 'merchs'

class MerchDetailView(generic.DetailView):
    model = Merch
    template_name = "merch/merch_detail.html"
