from django.contrib import admin

from .models import Restaurant, Location, JobPosting, Application

admin.site.register(Restaurant)
admin.site.register(Location)
admin.site.register(JobPosting)
admin.site.register(Application)