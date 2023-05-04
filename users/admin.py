from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *
from staffing_app.models import Location
from .forms import *

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ('email','first_name','last_name','is_staff','is_active','is_hiring_manager','is_restaurant_administrator',)
    list_filter = ('email','first_name','last_name','is_staff','is_active','is_hiring_manager','is_restaurant_administrator',)
    search_fields = ('email',)
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'location')}),
        ('Permissions', {
            'fields': ('is_staff', 'is_active', 'is_hiring_manager',
                       'is_restaurant_administrator', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                'email', 'first_name', 'last_name', 'password1', 'password2', 'is_staff',
                'is_active', 'is_hiring_manager', 'is_restaurant_administrator',
                'location', 'groups', 'user_permissions'
            )}
        ),
    )
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "location":
            kwargs["queryset"] = Location.objects.all()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(CustomUser, CustomUserAdmin)