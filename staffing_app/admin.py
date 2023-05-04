from django.contrib import admin
from .models import Location, JobPosting, Application

admin.site.register(Location)
admin.site.register(JobPosting)
admin.site.register(Application)