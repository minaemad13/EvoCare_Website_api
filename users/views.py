
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import FeedSerializer
from .models import Feedback
from rest_framework.decorators import api_view
# from rest_framework.response import JSONParser
# from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.parsers import JSONParser
# Create your views here.

class FeedView(viewsets.ModelViewSet):
    serializer_class = FeedSerializer
    queryset = Feedback.objects.all()

@api_view(['POST'])
def addFeed(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FeedSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data)
        return JsonResponse(serializer.errors, status=400)


        # return JsonResponse(serializer.errors, status=400)




# Create your views here.
