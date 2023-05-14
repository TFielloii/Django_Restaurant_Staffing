from datetime import datetime
from django.db import models

# Model for Restaurants
class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
# Model for Locations
class Location(models.Model):
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=20)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='locations')

    def __str__(self):
        return f'{self.restaurant}: {self.address}, {self.city} {self.state}'

# Model for Job Postings
class JobPosting(models.Model):
    title = models.CharField(max_length=200)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='jobposting')
    description = models.TextField()
    requirements = models.TextField()
    salary = models.DecimalField(max_digits=12, decimal_places=2)
    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

# Model for Applications
class Application(models.Model):
    from users.models import Applicant
    PENDING = 'pending'
    APPROVED = 'approved'
    REJECTED = 'rejected'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
    ]
    job_posting = models.ForeignKey(JobPosting, on_delete=models.CASCADE, related_name='applications')
    date_applied = datetime.now()
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE, related_name='applications')
    resume = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)
    
    def __str__(self):
        return f'{self.applicant.email} - {self.job_posting.title}'