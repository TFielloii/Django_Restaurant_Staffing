from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import *

router_users = routers.DefaultRouter()
router_users.register(r'applicants', ApplicantViewSet)
router_users.register(r'hiring_managers', HiringManagerViewSet)
router_users.register(r'restaurant_administrators', RestaurantAdministratorViewSet)
router_users.register(r'users', CustomUserViewSet)

urlpatterns = [
    path('api/', include(router_users.urls)),
    path('register', register, name='register'),
    path('login', custom_login, name='login'),
    path('logout', custom_logout, name='logout'),
    path('profile/<email>', profile, name='profile'),
    path("password_change", password_change, name="password_change"),
]