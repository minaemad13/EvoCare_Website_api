from rest_framework import serializers

from users.models import Appointement


class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Appointement
        fields=['User_id','dateandtime']