

from rest_framework import serializers
from users.models import UserProfile, Cars, Appointments


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['email', 'password']


class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointments
        fields = '__all__'
