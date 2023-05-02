from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from .forms import *

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email','first_name','last_name','is_staff','is_active','is_hiring_manager','is_restaurant_administrator',)
    list_filter = ('email','first_name','last_name','is_staff','is_active','is_hiring_manager','is_restaurant_administrator',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {
            'fields': ('is_staff', 'is_active', 'is_hiring_manager',
                       'is_restaurant_administrator', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                'email', 'password1', 'password2', 'is_staff',
                'is_active','is_hiring_manager','is_restaurant_administrator',
                'groups', 'user_permissions'
            )}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
admin.site.register(CustomUser, CustomUserAdmin)
