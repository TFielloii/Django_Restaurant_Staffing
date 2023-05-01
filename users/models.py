from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    STATUS = (
        ('applicant', 'applicant'),
        ('manager', 'manager'),
        ('admin', 'admin'),
    )
    email = models.EmailField(unique=True)
    status = models.CharField(max_length=100, choices=STATUS, default='applicant')
    is_applicant = models.BooleanField('applicant status', default=True)
    is_manager = models.BooleanField('manager status', default=False)
    is_admin = models.BooleanField('admin status', default=False)
    def __str__(self):
        return self.username

class Applicant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    email = models.EmailField()
    resume = models.TextField()
    '''
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class RestaurantAdministrator(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

class HiringManager(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)