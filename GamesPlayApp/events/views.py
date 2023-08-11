from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View

from GamesPlayApp.events.forms import EventForm, EventDeleteForm, EventGalleryImageForm
from GamesPlayApp.events.models import Event, EventGalleryImage, UserReview

from .forms import UserReviewForm


def submit_review(request, pk):
    event = get_object_or_404(Event, pk=pk)

    if request.method == 'POST':
        form = UserReviewForm(request.POST)
        if form.is_valid():
            rating = form.cleaned_data['rating']
            review_text = form.cleaned_data['review_text']
            user_review = UserReview.objects.create(event=event, user=request.user, rating=rating,
                                                    review_text=review_text)
            return redirect('event-details-page', pk=pk)
    else:
        form = UserReviewForm()

    context = {
        'event': event,
        'user_review_form': form,
    }

    return render(request, 'events/details-event.html', context)


def event_gallery(request, event_id):
    event = Event.objects.get(pk=event_id)
    gallery_images = EventGalleryImage.objects.filter(event=event)

    context = {
        'event': event,
        'gallery_images': gallery_images
    }

    return render(request, 'events/event_gallery.html', context)


def add_event_gallery_image(request, event_id):
    event = Event.objects.get(pk=event_id)

    if request.method == 'POST':
        form = EventGalleryImageForm(request.POST)
        if form.is_valid():
            gallery_image = form.save(commit=False)
            gallery_image.event = event
            gallery_image.save()
            return redirect('event-details-page', pk=event_id)
    else:
        form = EventGalleryImageForm()

    context = {
        'event': event,
        'form': form
    }

    return render(request, 'events/add_event_gallery_image.html', context)


class AttendEventView(View):
    def post(self, request, pk):
        event = get_object_or_404(Event, pk=pk)
        if request.user not in event.attendees.all():
            event.attendees.add(request.user)
        return redirect('event-details-page', pk=pk)


@login_required
def create_event(request):
    form = EventForm()

    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()

            return redirect('events-page')

    context = {
        'form': form
    }

    return render(request, 'events/create-event.html', context)


def event_details(request, pk):
    event = get_object_or_404(Event, pk=pk)

    is_attending = False

    if request.method == 'POST':
        if request.user.is_authenticated:
            if request.user in event.attendees.all():
                event.attendees.remove(request.user)
            else:
                event.attendees.add(request.user)
            return redirect('event-details-page', pk=pk)

    if request.user.is_authenticated and request.user in event.attendees.all():
        is_attending = True

    context = {
        'event': event,
        'is_attending': is_attending
    }

    return render(request, 'events/details-event.html', context)


def edit_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    form = EventForm(instance=event)

    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event.save()
            return redirect('events-page')

    context = {
        'form': form
    }

    return render(request, 'events/edit-event.html', context)


def delete_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    form = EventDeleteForm(instance=event)

    if request.method == 'POST':
        event.delete()
        return redirect('events-page')

    context = {
        'form': form
    }

    return render(request, 'events/delete-event.html', context)
