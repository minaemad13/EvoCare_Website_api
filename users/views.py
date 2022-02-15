from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view

from users.models import Appointement
from users.serializers import AppointmentSerializer


@api_view(['GET','POST', 'PUT', 'PATCH', 'DELETE'])
def student_detail(request):
    #student = info.objects.get(id=id)

    if request.method == 'POST':
        serializer = AppointmentSerializer(Appointement, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

