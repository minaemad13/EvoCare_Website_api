from rest_framework import serializers
from .models import ServicesPictures

class PicturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicesPictures
        fields = '__all__'
