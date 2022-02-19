from rest_framework import serializers
from .models import Feedback

class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('user_id','user_name','feedback')