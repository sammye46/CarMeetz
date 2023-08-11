from django.contrib.auth import get_user_model
from django.db import models

from GamesPlayApp.profile_car.models import Profile

# Create your models here.

User = get_user_model()


class Event(models.Model):
    user = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,

    )

    attendees = models.ManyToManyField(
        User,
        related_name='attended_events',
        blank=True)

    event_name = models.CharField(
        max_length=30,
        blank=False,
        null=False,

    )

    date = models.DateField(
        verbose_name="Date",
        blank=False,  # Set to True if the field is not required
        null=False,
    )

    time = models.TimeField()

    location = models.CharField(
        max_length=500,
        blank=False,
        null=False,

    )

    image_url = models.URLField(
        max_length=500,
        blank=False,
        null=False
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    class Meta:
        permissions = [
            ("can_change_featured_status", "Can change featured status of events"),
        ]


class EventGalleryImage(models.Model):
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE
    )
    image_url = models.URLField()


class UserReview(models.Model):
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )

    rating = models.PositiveIntegerField(
        choices=[(i, i) for i in range(1, 6)]
    )

    review_text = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Review by {self.user.username} for {self.event.event_name}"
