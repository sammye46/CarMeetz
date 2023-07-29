from django.urls import path
from GamesPlayApp.common import views

urlpatterns = [
    path('', views.index, name='home-page'),
    path('dashboard/', views.ListGamesView.as_view(), name='dashboard-page'),
]