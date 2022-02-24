from rest_framework import serializers
from .models import ServicesPictures, Packages

class PicturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicesPictures
        fields = '__all__'

class PackagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Packages
        fields = '__all__'