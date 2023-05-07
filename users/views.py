from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from rest_framework import viewsets

from .models import *
from .forms import *
from .decorators import user_not_authenticated
from .serializers import (ApplicantSerializer, HiringManagerSerializer,
                          RestaurantAdministratorSerializer, CustomUserSerializer)

# API views start here.
class ApplicantViewSet(viewsets.ModelViewSet):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer

class HiringManagerViewSet(viewsets.ModelViewSet):
    queryset = HiringManager.objects.all()
    serializer_class = HiringManagerSerializer

class RestaurantAdministratorViewSet(viewsets.ModelViewSet):
    queryset = RestaurantAdministrator.objects.all()
    serializer_class = RestaurantAdministratorSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

# View functions start here.
@user_not_authenticated
def custom_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                email=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Hello <b>{user.first_name}</b>! You have been logged in.")
                return redirect('homepage')
        else:
            for error in form.errors.values():
                messages.error(request, error) 
    form = UserLoginForm() 
    return render(
        request=request,
        template_name="login.html", 
        context={'form': form}
    )

# Custom Logout function for navbar.
@login_required
def custom_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("homepage")

@user_not_authenticated
def register(request):
    # Prevents authenticated user from creating additional accounts.
    if request.user.is_authenticated:
        return redirect("homepage")
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"New account created: {user.email}")
            return redirect('job-listings')
        else:
            for error in form.errors.values():
                messages.error(request, error)
    else:
        form = UserRegistrationForm()
    return render(
        request = request,
        template_name = "register.html",
        context={"form":form}
        )

def profile(request, email):
    if request.method == 'POST':
        user = request.user
        form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user_form = form.save()
            messages.success(request, f'{user_form}, Your profile has been updated!')
            return redirect('profile', user_form.email)
        for error in form.errors.values():
            messages.error(request, error)
    user = get_user_model().objects.filter(email=email).first()
    if user:
        form = UserUpdateForm(instance=user)
        return render(request, 'profile.html', context={'form': form})
    return redirect("homepage")

@login_required
def password_change(request):
    user = request.user
    if request.method == 'POST':
        form = SetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your password has been changed")
            return redirect('login')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    form = SetPasswordForm(user)
    return render(request, 'password_reset_confirm.html', {'form': form})