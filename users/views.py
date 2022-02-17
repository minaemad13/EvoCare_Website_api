from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from users.models import Appointments
from users.serializers import AppointmentSerializer


class GetAppointement(viewsets.ModelViewSet):
    queryset = Appointments.objects.raw('SELECT "Date_Time" , id FROM users_appointments')
    serializer_class = AppointmentSerializer

@api_view(['POST'])
def Take_Appointement(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AppointmentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data)
        return JsonResponse(serializer.errors, status=400)
