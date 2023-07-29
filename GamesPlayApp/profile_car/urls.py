from django.urls import path
from GamesPlayApp.profile_car import views

urlpatterns = [
    path('create/', views.UserRegisterView.as_view(), name='create-profile'),
    path('login/', views.UserLoginView.as_view(), name='login-profile'),
    path('logout/', views.UserLogoutView.as_view(), name='logout-profile'),
    # path('create/', views.create_profile, name='create-profile'),
    path('details/<int:pk>/', views.ProfileDetailsView.as_view(), name='profile-details'),
    path('edit/', views.UserEditView.as_view(), name='edit-profile'),
    path('delete/', views.ProfileDeleteView.as_view(), name='delete-profile'),
]
