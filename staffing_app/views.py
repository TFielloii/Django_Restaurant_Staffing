from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse_lazy
from .forms import ApplicationForm
from .models import *
from django.contrib.auth.mixins import UserPassesTestMixin

class RestaurantAdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and hasattr(self.request.user, 'is_restaurant_administrator')
class HiringManagerRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and hasattr(self.request.user, 'is_hiring_manager')

# Create your views here.
def homepage(request):
    return render(request=request,
                  template_name='home.html',
                  )

# Views for locations
class LocationListView(RestaurantAdminRequiredMixin, ListView):
    model = Location
    template_name = 'location/location_list.html'
    context_object_name = 'locations'
class LocationCreateView(RestaurantAdminRequiredMixin, CreateView):
    model = Location
    fields = ['name','number','street_address','city','state','phone']
    template_name = 'location/location_create.html'
    success_url = reverse_lazy('location-list')
class LocationDetailView(RestaurantAdminRequiredMixin, DetailView):
    model = Location
    template_name = 'location/location_detail.html'
class LocationUpdateView(RestaurantAdminRequiredMixin, UpdateView):
    model = Location
    fields = ['name','number','street_address','city','state','phone']
    template_name = 'location/location_update.html'
    success_url = reverse_lazy('location-list')
class LocationDeleteView(RestaurantAdminRequiredMixin, DeleteView):
    model = Location
    template_name = 'location/location_delete.html'
    success_url = reverse_lazy('location-list')

# Views for Job Posting model
class JobPostingListView(ListView):
    model = JobPosting
    template_name = 'jobposting/jobposting_list.html'
    context_object_name = 'job_postings'
class JobPostingCreateView(RestaurantAdminRequiredMixin, CreateView):
    model = JobPosting
    fields = ['title','loc','descr','requirements','salary']
    template_name = 'jobposting/jobposting_create.html'
    success_url = reverse_lazy('jobposting-list')
class JobPostingDetailView(DetailView):
    model = JobPosting
    template_name = 'jobposting/jobposting_detail.html'
    success_url = reverse_lazy('application-create')
class JobPostingUpdateView(RestaurantAdminRequiredMixin, UpdateView):
    model = JobPosting
    fields = ['title','loc','descr','requirements','salary']
    template_name = 'jobposting/jobposting_update.html'
    success_url = reverse_lazy('jobposting-list')
class JobPostingDeleteView(RestaurantAdminRequiredMixin, DeleteView):
    model = JobPosting
    template_name = 'jobposting/jobposting_delete.html'
    success_url = reverse_lazy('jobposting-list')

# Views for Application model
class ApplicationListView(HiringManagerRequiredMixin, ListView):
    model = Application
    template_name = 'application/application_list.html'
    context_object_name = 'applications'
    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(hiring_manager__location=self.request.user.is_hiring_manager.location)
        return qs
class ApplicationCreateView(CreateView):
    model = Application
    form_class = ApplicationForm
    success_url = reverse_lazy('jobposting-list')
    template_name = 'application/application_create.html'
class ApplicationDetailView(DetailView):
    model = Application
    template_name = 'application/application_detail.html'
class ApplicationUpdateView(HiringManagerRequiredMixin, UpdateView):
    model = Application
    fields = ['job_posting','applicant','hiring_manager','resume','status']
    template_name = 'application/application_update.html'
    success_url = reverse_lazy('application-list')
    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(hiring_manager__location=self.request.user.is_hiring_manager.location)
        return qs
class ApplicationDeleteView(HiringManagerRequiredMixin, DeleteView):
    model = Application
    template_name = 'application/application_delete.html'
    success_url = reverse_lazy('application-list')
    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(hiring_manager__location=self.request.user.is_hiring_manager.location)
        return qs


# Modules for applicants to apply
@login_required
def apply_to_job(request, job_id):
    job_posting = get_object_or_404(JobPosting, id=job_id)
    form = ApplicationForm()

    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.job_posting = job_posting
            application.applicant = request.user.applicant
            application.save()
            return redirect('job_postings')

    context = {
        'form': form,
        'job_posting': job_posting,
    }
    return render(request, 'application/application_create.html', context)