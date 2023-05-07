"""
URL configuration for Django_Restaurant_Staffing project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers

from staffing_app.views import LocationViewSet, JobPostingViewSet, ApplicationViewSet
from users.views import ApplicantViewSet, HiringManagerViewSet, RestaurantAdministratorViewSet, CustomUserViewSet

# Define router for API endpoints
router = routers.DefaultRouter()
router.register(r'locations', LocationViewSet)
router.register(r'job_postings', JobPostingViewSet)
router.register(r'applications', ApplicationViewSet)
router.register(r'applicants', ApplicantViewSet)
router.register(r'hiring_managers', HiringManagerViewSet)
router.register(r'restaurant_administrators', RestaurantAdministratorViewSet)
router.register(r'users', CustomUserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('api/', include(router.urls)),
    path('', include('staffing_app.urls')),
    path('', include('users.urls')),
]

# Serve media files in development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)