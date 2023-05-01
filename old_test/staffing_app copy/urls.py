from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name='homepage'),
    path('locations/', LocationListView.as_view(), name='location-list'),
    path('locations/create/', LocationCreateView.as_view(), name='location-create'),
    path('locations/<int:pk>/', LocationDetailView.as_view(), name='location-detail'),
    path('locations/<int:pk>/update/', LocationUpdateView.as_view(), name='location-update'),
    path('locations/<int:pk>/delete/', LocationDeleteView.as_view(), name='location-delete'),

    path('job-postings/', JobPostingListView.as_view(), name='jobposting-list'),
    path('job-postings/create/', JobPostingCreateView.as_view(), name='jobposting-create'),
    path('job-postings/<int:pk>/', JobPostingDetailView.as_view(), name='jobposting-detail'),
    path('job-postings/<int:pk>/update/', JobPostingUpdateView.as_view(), name='jobposting-update'),
    path('job-postings/<int:pk>/delete/', JobPostingDeleteView.as_view(), name='jobposting-delete'),

    path('applications/', ApplicationListView.as_view(), name='application-list'),
    path('applications/create/', ApplicationCreateView.as_view(), name='application-create'),
    path('applications/<int:job_id>/', apply_to_job, name='apply_to_job'),
    path('applications/<int:pk>/', ApplicationDetailView.as_view(), name='application-detail'),
    path('applications/<int:pk>/update/', ApplicationUpdateView.as_view(), name='application-update'),
    path('applications/<int:pk>/delete/', ApplicationDeleteView.as_view(), name='application-delete'),
]