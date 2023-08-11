from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User, Group
from GamesPlayApp.profile_car.models import Profile  # Import your Profile model

# Customize UserAdmin
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')

# Register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Register your custom admin groups
admin.site.register(Group)

# Register your Profile model
admin.site.register(Profile)
