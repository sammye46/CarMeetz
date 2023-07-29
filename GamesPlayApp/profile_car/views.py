from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views, login, authenticate
from django.views.generic import DetailView, UpdateView, DeleteView, ListView

from GamesPlayApp.car.models import Car
from GamesPlayApp.profile_car.forms import ProfileForm, ProfileEditForm, LoginForm
from GamesPlayApp.profile_car.models import Profile
from django.views import generic as views

class UserRegisterView(views.CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'profile_car/create-profile.html'
    success_url = reverse_lazy('home-page')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)  # Automatically log in the user
        return response
class UserLoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'profile_car/login-profile.html'
    # next_page = reverse_lazy('home-page')

class UserLogoutView(auth_views.LogoutView):
    pass
# Create your views here.
# def create_profile(request):
#     form = ProfileForm()
#
#     if request.method == 'POST':
#         form = ProfileForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home-page')
#
#     context = {
#         'form': form
#     }
#     return render(request, 'profile_car/create-profile.html', context)


class ProfileDetailsView(DetailView):
    template_name = 'profile_car/details-profile.html'
    model = Profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.object
        cars = Car.objects.filter(user=self.request.user)

        context['profile'] = profile
        context['cars'] = cars

        return context
# def profile_details(request):
#     profile = Profile.objects.all()
#     games = Game.objects.all()
#
#     average_rating = sum(x.rating for x in games) / len(games) if games else 0.0
#
#
#
#     context = {
#         'profile': profile,
#         'games': games,
#         'average_rating': average_rating
#     }
#     return render(request, 'profile_car/details-profile.html', context)


class UserEditView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'profile_car/edit-profile.html'

    def get_object(self, queryset=None):
        # Retrieve the profile associated with the currently logged-in user
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.object.pk})

# def edit_profile(request):
#     profile = Profile.objects.first()
#     form = ProfileEditForm(instance=profile)
#     if request.method == 'POST':
#         form = ProfileEditForm(request.POST, instance=profile)
#         if form.is_valid():
#             form.save()
#             return redirect('profile-details')
#
#     context = {
#         'form': form,
#
#     }
#     return render(request, 'profile_car/edit-profile.html', context)


class ProfileDeleteView(DeleteView):
    model = Profile
    success_url = reverse_lazy('home-page')  # Replace with your desired success URL
    template_name = 'profile_car/delete-profile.html'

    def get_object(self, queryset=None):
        # Return the profile associated with the currently logged-in user
        return self.request.user

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        cars = Car.objects.all()  # Retrieve the associated cars
        cars.delete()
        self.object.delete()
        return self.get_success_url()
# def delete_profile(request):
#     profile = Profile.objects.first()
#     games = Game.objects.all()
#     if request.method == 'POST':
#         profile.delete()
#         games.delete()
#         return redirect('home-page')
#     context = {
#         'profile': profile
#     }
#     return render(request, 'profile_car/delete-profile.html', context)
