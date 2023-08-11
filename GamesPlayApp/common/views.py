from django.shortcuts import render
from django.views.generic import ListView

from GamesPlayApp.car.models import Car
from GamesPlayApp.events.models import Event


# Create your views here.
def index(request):
    return render(request, 'common/home-page.html')


class ListGamesView(ListView):
    template_name = 'common/dashboard.html'
    model = Car

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cars = Car.objects.filter(user=self.request.user)

        context['cars'] = cars
        return context

class ListEventsView(ListView):
    template_name = 'common/events.html'
    model = Event

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        events = Event.objects.all()

        context['events'] = events
        return context