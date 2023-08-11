from django.urls import path
from GamesPlayApp.events import views


urlpatterns = [
    path('create/', views.create_event, name='create-event-page'),
    path('details/<int:pk>/', views.event_details, name='event-details-page'),
    path('edit/<int:pk>/', views.edit_event, name='edit-event-page'),
    path('delete/<int:pk>/', views.delete_event, name='delete-event-page'),
    path('attend/<int:pk>/', views.event_details, name='attend-event'),
    path('add_image/<int:event_id>/', views.add_event_gallery_image, name='add-event-gallery-image'),
    path('event_gallery/<int:event_id>/', views.event_gallery, name='event-gallery'),
    path('submit-review/<int:pk>/', views.submit_review, name='submit-review'),


]
