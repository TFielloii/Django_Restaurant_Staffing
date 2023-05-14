from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser
from staffing_app.models import Location, Restaurant

class CustomUserAdmin(UserAdmin):
    # Set the custom forms to be used for adding and changing users
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    # Set the fields to display in the list view
    list_display = (
        'email',
        'first_name',
        'last_name',
        'is_staff',
        'is_active',
        'is_hiring_manager',
        'is_restaurant_administrator',
    )

    # Set the filters to use in the list view
    list_filter = (
        'email',
        'first_name',
        'last_name',
        'is_staff',
        'is_active',
        'is_hiring_manager',
        'is_restaurant_administrator',
    )

    search_fields = ('email',)
    ordering = ('email',)

    # Sets the fieldsets to use in the add and change views.
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {
            'fields': ('is_staff', 'is_active', 'is_restaurant_administrator',
                       'is_hiring_manager', 'groups', 'user_permissions'),
        }),
    )

    # Sets the add fieldsets to use in the add view.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'first_name',
                'last_name',
                'password1',
                'password2',
                'is_staff',
                'is_active',
                'is_hiring_manager',
                'is_restaurant_administrator',
                'restaurant',
                'location',
                'groups',
                'user_permissions',
            ),
        }),
    )
    
    class Media:
        js = ('admin/js/user-admin.js',)

    # Override to ensure the saved restaurant is saved in the admin screen.
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'restaurant':
            kwargs['queryset'] = Restaurant.objects.all()
        if db_field.name == 'location':
            kwargs['queryset'] = Location.objects.all()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


# Registers the custom user model with the custom admin class.
admin.site.register(CustomUser, CustomUserAdmin)