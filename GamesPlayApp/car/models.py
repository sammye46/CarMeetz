from django.contrib.auth import get_user_model
from django.db import models
from django.core import validators

from GamesPlayApp.profile_car.models import Profile

# Create your models here.

User = get_user_model()


class Car(models.Model):
    user = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,

    )

    brand = models.CharField(
        max_length=30,
        blank=False,
        null=False,

    )

    model = models.CharField(
        max_length=30,
        blank=False,
        null=False,
    )

    priority = models.CharField(
        max_length=30,
        blank=False,
        null=False,
        choices=(
            ('Low', 'Low'),
            ('Medium', 'Medium'),
            ('High', 'High'),
        )
    )

    image_url = models.URLField(
        blank=False,
        null=False
    )

    summary = models.TextField(
        blank=True,
        null=True
    )
