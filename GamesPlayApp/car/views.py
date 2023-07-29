from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from GamesPlayApp.car.forms import CarForm, CarDeleteForm
from GamesPlayApp.car.models import Car
from GamesPlayApp.profile_car.models import Profile


# Create your views here.

@login_required
def create_car(request):
    form = CarForm()

    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            car = form.save(commit=False)
            car.user = request.user  # Accessing the profile from the User instance
            car.save()

            return redirect('dashboard-page')

    context = {
        'form': form
    }

    return render(request, 'car/create-car.html', context)


def car_details(request, pk):
    car = get_object_or_404(Car, pk=pk)

    context = {
        'car': car
    }
    return render(request, 'car/details-car.html', context)


def edit_car(request, pk):
    car = get_object_or_404(Car, pk=pk)
    form = CarForm(instance=car)

    if request.method == "POST":
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('dashboard-page')

    context = {
        'form': form
    }
    return render(request, 'car/edit-car.html', context)


def delete_car(request, pk):
    car = get_object_or_404(Car, pk=pk)
    form = CarDeleteForm(instance=car)

    if request.method == "POST":
        car.delete()
        return redirect('dashboard-page')

    context = {
        'form': form
    }

    return render(request, 'car/delete-car.html', context)
