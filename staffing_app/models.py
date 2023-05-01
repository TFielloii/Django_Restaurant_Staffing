import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Location(models.Model):
    name = models.CharField(max_length=50)
    number = models.PositiveIntegerField()
    street_address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    phone = models.CharField(max_length=11)
    def __str__(self):
        return self.name

class JobPosting(models.Model):
    title = models.CharField(max_length=200)
    loc = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='jobposting')
    descr = models.TextField()
    requirements = models.TextField()
    salary = models.DecimalField(max_digits=12, decimal_places=2)
    def __str__(self):
        return self.title

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

class Application(models.Model):
    job_posting = models.ForeignKey(JobPosting, on_delete=models.CASCADE, related_name='applications')
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE, related_name='applications')
    hiring_manager = models.ForeignKey(HiringManager, on_delete=models.CASCADE)
    email = models.EmailField()
    resume = models.TextField()
    def __str__(self):
        return f'{self.email} - {self.job_posting.title}'