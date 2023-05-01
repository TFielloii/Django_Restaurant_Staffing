import datetime
from django.db import models
from users.models import CustomUser

class Location(models.Model):
    name = models.CharField(max_length=50)
    number = models.PositiveIntegerField(unique=True)
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
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    resume = models.TextField()

class RestaurantAdministrator(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

class HiringManager(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

class Application(models.Model):
    PENDING = 'pending'
    APPROVED = 'approved'
    REJECTED = 'rejected'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
    ]
    job_posting = models.ForeignKey(JobPosting, on_delete=models.CASCADE, related_name='applications')
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE, related_name='applications')
    hiring_manager = models.ForeignKey(HiringManager, on_delete=models.CASCADE)
    resume = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)
    def __str__(self):
        return f'{self.applicant.email} - {self.job_posting.title}'