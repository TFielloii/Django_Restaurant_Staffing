from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView
from django.contrib import messages
from django.urls import reverse_lazy
from users.models import Applicant
from django.contrib.auth.mixins import UserPassesTestMixin
from django.conf import settings
from django.core.mail import send_mail
from django.views.decorators.http import require_POST
from rest_framework import viewsets
from .serializers import RestaurantSerializer, LocationSerializer, JobPostingSerializer, ApplicationSerializer
from .forms import ApplicationForm, JobPostingForm, LocationForm
from .models import Restaurant, Location, JobPosting, Application

# API CRUD views.
class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class JobPostingViewSet(viewsets.ModelViewSet):
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

# Mixins for restricting specific site access.
class AuthenticationRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated
class RestaurantAdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_restaurant_administrator
class HiringManagerRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_hiring_manager

# Basic homepage view.
def homepage(request):
    return render(request=request,
                  template_name='home.html',
                  )

# Views for locations.
class LocationListView(RestaurantAdminRequiredMixin, ListView):
    model = Location
    template_name = 'location/location_list.html'
    context_object_name = 'locations'
class LocationCreateView(RestaurantAdminRequiredMixin, CreateView):
    model = Location
    form_class = LocationForm
    template_name = 'location/location_create.html'
    success_url = reverse_lazy('location_list')
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['restaurant'] = self.request.user.restaurant
        return kwargs
class LocationDetailView(RestaurantAdminRequiredMixin, DetailView):
    model = Location
    template_name = 'location/location_detail.html'
class LocationUpdateView(RestaurantAdminRequiredMixin, UpdateView):
    model = Location
    form_class = LocationForm
    template_name = 'location/location_update.html'
    success_url = reverse_lazy('location_list')
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['restaurant'] = self.request.user.restaurant
        return kwargs
class LocationDeleteView(RestaurantAdminRequiredMixin, DeleteView):
    model = Location
    template_name = 'location/location_delete.html'
    success_url = reverse_lazy('location_list')

# Views for Job Posting model.
class JobPostingListView(AuthenticationRequiredMixin, ListView):
    model = JobPosting
    template_name = 'jobposting/jobposting_list.html'
    context_object_name = 'job_postings'
class JobPostingCreateView(RestaurantAdminRequiredMixin, CreateView):
    model = JobPosting
    form_class = JobPostingForm
    template_name = 'jobposting/jobposting_create.html'
    success_url = reverse_lazy('jobposting_list')
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['restaurant'] = self.request.user.restaurant
        return kwargs
class JobPostingDetailView(AuthenticationRequiredMixin, DetailView):
    model = JobPosting
    template_name = 'jobposting/jobposting_detail.html'
    success_url = reverse_lazy('application_create')
class JobPostingUpdateView(RestaurantAdminRequiredMixin, UpdateView):
    model = JobPosting
    fields = ['title','location','description','requirements','salary']
    template_name = 'jobposting/jobposting_update.html'
    success_url = reverse_lazy('jobposting_list')
class JobPostingDeleteView(RestaurantAdminRequiredMixin, DeleteView):
    model = JobPosting
    template_name = 'jobposting/jobposting_delete.html'
    success_url = reverse_lazy('jobposting_list')

# Views for Application model.
class ApplicationListView(HiringManagerRequiredMixin, ListView):
    model = Application
    template_name = 'application/application_list.html'
    context_object_name = 'applications'
class ApplicationCreateView(AuthenticationRequiredMixin, CreateView):
    model = Application
    form_class = ApplicationForm
    success_url = reverse_lazy('jobposting_list')
    template_name = 'application/application_create.html'
class ApplicationDetailView(HiringManagerRequiredMixin, DetailView):
    model = Application
    template_name = 'application/application_detail.html'
class ApplicationUpdateView(HiringManagerRequiredMixin, UpdateView):
    model = Application
    fields = ['job_posting','applicant','resume','status']
    template_name = 'application/application_update.html'
    success_url = reverse_lazy('application_list')
class ApplicationDeleteView(HiringManagerRequiredMixin, DeleteView):
    model = Application
    template_name = 'application/application_delete.html'
    success_url = reverse_lazy('application_list')


# The application view
@login_required
def apply_to_job(request, job_id):
    job_posting = get_object_or_404(JobPosting, id=job_id)
    form = ApplicationForm()
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.job_posting = job_posting
            try:
                applicant = request.user.applicant
            except:
                applicant = Applicant.objects.create(user=request.user)
            application.applicant = applicant
            application.save()
            messages.success(request, "Your resume has been submitted successfully. Please wait for an email from our hiring manager.")
            return redirect('jobposting_list')
    context = {
        'form': form,
        'job_posting': job_posting,
    }
    return render(request, 'application/application_create.html', context)

# Sends email out to applicants
@require_POST
def application_email(request, app_id):
    application = get_object_or_404(Application, id=app_id)
    current_status = application.status

    if request.POST.get('action') == 'update_status':
        new_status = request.POST.get('status')
        if new_status != current_status:
            application.status = new_status
            application.save()

            if application.status == 'APPROVED':
                subject = 'Congratulations'
                message = 'Dear {} {},\n\nYou have been accepted for the position of {}, at {}. Please report to work in 3 days and if you have any questions please reach out.\n\nWelcome aboard,\n{} {}'.format(
                    application.applicant.user.first_name, application.applicant.user.last_name, application.job_posting.title,
                    application.job_posting.location, request.user.first_name, request.user.last_name)
            elif application.status == 'REJECTED':
                subject = "We're sorry."
                message = 'Dear {} {},\n\nUnfortunately, you have not been accepted for the position of {}, at {}.\n\nGood luck in your future endeavors,\n{} {}'.format(
                    application.applicant.user.first_name, application.applicant.user.last_name, application.job_posting.title,
                    application.job_posting.location, request.user.first_name, request.user.last_name)
            else:
                subject = "We've changed our minds."
                message = 'Dear {} {},\n\nWe decided to change our minds about considering you for the position of {}, at {}.\n\nYour move,\n{} {}'.format(
                    application.applicant.user.first_name, application.applicant.user.last_name, application.job_posting.title,
                    application.job_posting.location, request.user.first_name, request.user.last_name)

            email_from = settings.DEFAULT_FROM_EMAIL
            recipient_list = [application.applicant.user.email]
            send_mail(subject, message, email_from, recipient_list)
            messages.success(request, "The updated status has been emailed to the applicant.")
        else:
            messages.warning(request, "The status has not been changed.")
    
    return redirect('application_list')