from django.urls import path

from .views import *

urlpatterns = [
    path('', homepage, name='homepage'),

    # URL patterns for Location-related views
    path('locations/', LocationListView.as_view(), name='location_list'),
    path('locations/create/', LocationCreateView.as_view(), name='location_create'),
    path('locations/<int:pk>/', LocationDetailView.as_view(), name='location_detail'),
    path('locations/<int:pk>/update/', LocationUpdateView.as_view(), name='location_update'),
    path('locations/<int:pk>/delete/', LocationDeleteView.as_view(), name='location_delete'),

    # URL patterns for JobPosting-related views
    path('job_postings/', JobPostingListView.as_view(), name='jobposting_list'),
    path('job_postings/create/', JobPostingCreateView.as_view(), name='jobposting_create'),
    path('job_postings/<int:pk>/', JobPostingDetailView.as_view(), name='jobposting_detail'),
    path('job_postings/<int:pk>/update/', JobPostingUpdateView.as_view(), name='jobposting_update'),
    path('job_postings/<int:pk>/delete/', JobPostingDeleteView.as_view(), name='jobposting_delete'),

    # URL patterns for Application-related views
    path('applications/', ApplicationListView.as_view(), name='application_list'),
    path('applications/create/', ApplicationCreateView.as_view(), name='application_create'),
    path('applications/<int:job_id>/apply', apply_to_job, name='apply_to_job'),
    path('applications/<int:app_id>/email/', application_email, name='application_email'),
    path('applications/<int:pk>/details/', ApplicationDetailView.as_view(), name='application_detail'),
    path('applications/<int:pk>/update/', ApplicationUpdateView.as_view(), name='application_update'),
    path('applications/<int:pk>/delete/', ApplicationDeleteView.as_view(), name='application_delete'),
]