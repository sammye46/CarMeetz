from django.contrib.auth.models import AbstractUser
from django.db import models
# from django.core import validators


# Create your models here.
class Profile(AbstractUser):
    CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Do not show', 'Do not show'),
    )

    email = models.EmailField(
        blank=False,
        null=False,
        unique=True
    )

    # age = models.IntegerField(
    #     blank=False,
    #     null=False,
    #     validators=[validators.MinValueValidator(12)]
    # )

    # password = models.CharField(
    #     max_length=30,
    #     blank=False,
    #     null=False
    # )

    profile_picture = models.URLField(
        blank=True,
        null=True
    )

