# Generated by Django 4.2.2 on 2023-08-08 17:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=30)),
                ('date', models.DateField(verbose_name='Date')),
                ('time', models.TimeField()),
                ('location', models.CharField(max_length=500)),
                ('image_url', models.URLField()),
                ('description', models.TextField(blank=True, null=True)),
                ('attendees', models.ManyToManyField(blank=True, related_name='attended_events', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
