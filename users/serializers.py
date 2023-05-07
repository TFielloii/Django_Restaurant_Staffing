from rest_framework import serializers

from .models import Applicant, HiringManager, RestaurantAdministrator, CustomUser

# Serializers for the Users models.
class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = '__all__'

class HiringManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = HiringManager
        fields = '__all__'

class RestaurantAdministratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantAdministrator
        fields = '__all__'

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'