from rest_framework import serializers

from users.models import Appointments


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointments
        fields = '__all__'
