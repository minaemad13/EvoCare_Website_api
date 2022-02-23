from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from users.models import UserProfile, Appointments,Feedback
from django.shortcuts import render
from users.serializers import UserLoginSerializer, UserProfileSerializer, AppointmentSerializer,FeedSerializer
from rest_framework import status, viewsets
 
# Create your views here.


@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserProfileSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'result': "successfully"})
        return JsonResponse(serializer.errors, status=400)


@api_view(['POST'])
def MyLogin(request):
    if request.method == 'POST':
        email = request.data['email']
        password = request.data['password']
        try:
            user = UserProfile.objects.get(email=email, password=password)
            if user:
                return JsonResponse({'result': "1", 'message': "login successful", "user_id": user.id})
        except UserProfile.DoesNotExist:
            return JsonResponse({'result': "2", 'message': "the email or password is not correct"}, status=400)

    return JsonResponse({'result': "failed "}, status=400)


@api_view(['PUT'])
def EditProfile(request, id):
    if request.method == 'PUT':
        user = UserProfile.objects.get(id=id)
        serializer = UserLoginSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
          
          
          
class GetAppointement(viewsets.ModelViewSet):
    queryset = Appointments.objects.all()
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
