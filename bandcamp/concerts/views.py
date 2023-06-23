from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from . models import Concert
from . forms import ConcertForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse, reverse_lazy
from django.http import JsonResponse
from django.contrib import messages


class ConcertListView(generic.ListView):
    model = Concert
    template_name = "concert/concert_view.html"
    context_object_name = 'concerts'

class ConcertCreateView(LoginRequiredMixin, generic.CreateView):
    model = Concert
    form_class = ConcertForm
    template_name = 'concert/concert_form.html'
    success_url = reverse_lazy('concerts')

    def form_valid(self, form):
        city_name = form.cleaned_data.get('city_name')
        venue_name = form.cleaned_data.get('venue_name')

        if not city_name or not venue_name:
            form.add_error(None, "City name and venue name are required.")
            return self.form_invalid(form)

        return super().form_valid(form)

class ConcertUpdateDeleteView(LoginRequiredMixin, generic.UpdateView):
    model = Concert
    template_name = 'concert/concert_update.html'
    success_url = reverse_lazy('concerts') 
    form_class = ConcertForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        concert = self.get_object()
        context['concert'] = concert
        return context

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):  
        if 'delete' in request.POST:
            return self.delete(request, *args, **kwargs)
        else:
            return super().post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        album = self.get_object()
        album.delete()
        return redirect(self.success_url)

    def get_object(self, queryset=None):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=self.kwargs['pk'])
        return obj