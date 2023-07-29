from django.shortcuts import render
from django.views.generic import ListView

from GamesPlayApp.car.models import Car



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