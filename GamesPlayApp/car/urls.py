from django.urls import path
from GamesPlayApp.car import views

urlpatterns = [
    path('create/', views.create_car, name='create-car-page'),
    path('details/<int:pk>/', views.car_details, name='car-details-page'),
    path('edit/<int:pk>/', views.edit_car, name='edit-car-page'),
    path('delete/<int:pk>/', views.delete_car, name='delete-car-page'),
]