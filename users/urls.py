from django.urls import path
from .views import *

urlpatterns = [
    path('register', register, name='register'),
    path('login', custom_login, name='login'),
    path('logout', custom_logout, name='logout'),
    path('profile/<email>', profile, name='profile'),
    path("password_change", password_change, name="password_change"),
]