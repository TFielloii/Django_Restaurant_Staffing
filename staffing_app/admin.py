from django.contrib import admin
from .models import Location, JobPosting, Application, Applicant

admin.site.register(Location)
admin.site.register(JobPosting)
admin.site.register(Application)