from typing import Any, Dict, Optional
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db import models
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from .models import Merch
from .forms import MerchForm

@login_required
def merch(request):
    if request.method == 'POST':
        form = MerchForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('merch')
        else:
            print(form.errors)
    else:
        form = MerchForm
    return render(request, 'merch/manage_merch.html', {'form': form})

class MerchListView(generic.ListView):
    model = Merch
    template_name = "merch/merch.html"
    context_object_name = 'merchs'

class MerchDetailView(generic.DetailView):
    model = Merch
    template_name = "merch/merch_detail.html"

class MerchUpdateView(generic.UpdateView, LoginRequiredMixin):
    model = Merch
    template_name = "merch/merch_update.html"
    success_url = reverse_lazy('merch')
    form_class = MerchForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['merch'] = self.object
        return context

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        if 'delete' in request.POST:
            return self.delete(request, *args, **kwargs)
        else:
            return super().post(request, *args, **kwargs)
        
    def delete(self, request, *args, **kwargs):
        merch = self.get_object()
        merch.delete()
        return redirect(self.success_url)

    def get_object(self, queryset=None):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=self.kwargs['pk'])
        return obj