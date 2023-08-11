from django.contrib import admin
from .models import Event  # Import your models

@admin.register(Event)  # Register your model
class EventAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'date', 'location')  # Customize list display
    list_filter = ('date',)  # Add filters
    search_fields = ('event_name', 'location')  # Add search fields
    actions = ['mark_featured', 'mark_not_featured']

    def mark_featured(self, request, queryset):
        queryset.update(is_featured=True)
    mark_featured.short_description = "Mark selected events as featured"

    def mark_not_featured(self, request, queryset):
        queryset.update(is_featured=False)
    mark_not_featured.short_description = "Mark selected events as not featured"

    def get_model_perms(self, request):
        perms = super().get_model_perms(request)
        perms.update({'change_featured_status': request.user.has_perm('events.change_featured_status')})
        return perms