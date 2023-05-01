from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self, email, is_hiring_manager=False, is_restaurant_administrator=False, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        if is_hiring_manager:
            from staffing_app.models import HiringManager
            hiring_manager = HiringManager.objects.create(user=user)
            hiring_manager.save()
        elif is_restaurant_administrator:
            from staffing_app.models import RestaurantAdministrator
            restaurant_administrator = RestaurantAdministrator.objects.create(user=user)
            restaurant_administrator.save()
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault("is_active", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_hiring_manager = models.BooleanField(default=False)
    is_restaurant_administrator = models.BooleanField(default=False)
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']
    def has_module_perms(self, app_label):
        return self.is_staff
    def has_perm(self, perm, obj=None):
        return self.is_staff
    def __str__(self):
        return self.email