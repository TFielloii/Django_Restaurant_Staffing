from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from staffing_app.models import Location

class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name='', last_name='', is_hiring_manager=False, is_restaurant_administrator=False, password=None, location=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save()
        if is_hiring_manager:
            hiring_manager = HiringManager.objects.create(user=user, location=location)
            hiring_manager.save()
        elif is_restaurant_administrator:
            restaurant_administrator = RestaurantAdministrator.objects.create(user=user, location=location)
            restaurant_administrator.save()
        else:
            applicant = Applicant.objects.create(user=user)
            applicant.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password=password, **extra_fields)

class CustomUser(AbstractUser):
    """This represents a User object within our system"""
    username = None
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_hiring_manager = models.BooleanField(default=False)
    is_restaurant_administrator = models.BooleanField(default=False)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

class Applicant(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

class RestaurantAdministrator(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

class HiringManager(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
