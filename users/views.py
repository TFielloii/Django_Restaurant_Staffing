from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import *
from .forms import *
from .decorators import user_not_authenticated

# Create your views here.
@user_not_authenticated
def custom_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                backend='users.backends.EmailBackend'
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Hello <b>{user.first_name}</b>! You have been logged in")
                return redirect('homepage')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error) 
    form = UserLoginForm() 
    return render(
        request=request,
        template_name="login.html", 
        context={'form': form}
        )

@login_required
def custom_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("homepage")

@user_not_authenticated
def register(request):
    # Logged in user can't register a new account
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"New account created: {user.email}")
            return redirect('jobposting-list')
        else:
            for error in list(form.errors.values()):
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
        for error in list(form.errors.values()):
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
    return render(request, 'password_reset.html', {'form': form})