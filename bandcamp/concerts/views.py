from django.shortcuts import render, redirect
from django.views import generic
from . models import Concert
from . forms import ConcertForm, ConcertVenueForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse, reverse_lazy
from django.http import JsonResponse


class ConcertListView(generic.ListView):
    model = Concert
    template_name = "concert_view.html"
    context_object_name = 'concerts'


def create_venue(request):
    if request.method == 'POST':
        form = ConcertVenueForm(request.POST)
        if form.is_valid():
            venue = form.save()
            return JsonResponse({'success': True, 'venue_id': venue.pk})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = ConcertVenueForm()

    return render(request, 'create_venue.html', {'form': form})


class ConcertCreateView(LoginRequiredMixin, generic.CreateView):
    model = Concert
    form_class = ConcertForm
    template_name = 'concert_form.html'
    success_url = reverse_lazy('concerts')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['venue_form'] = ConcertVenueForm()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        venue_form = context['venue_form']
        
        if form.is_valid() and venue_form.is_valid():
            self.object = form.save()
            venue = venue_form.save()
            # Associate the newly created venue with the concert
            self.object.venue = venue
            self.object.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)