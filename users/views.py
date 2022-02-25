from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from users.models import UserProfile, Appointments, Feedback

from users.serializers import UserLoginSerializer, UserProfileSerializer, AppointmentSerializer, FeedSerializer
from rest_framework import status, viewsets
import jwt, datetime


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
                payload = {
                    'id': user.id,
                    'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
                    'iat': datetime.datetime.utcnow()
                }
                token = jwt.encode(payload,'django-insecure-!^f2ot^_+g!g9$0j@eb8hvhcw+63*hth0=#wo*+2x#45sx95x$', algorithm='HS256').decode('utf-8')
                return JsonResponse({'jwt': token}, status=200)
                # return JsonResponse({'result': "1", 'message': "login successful", "user_id": user.id})
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
        return JsonResponse(serializer.errors, status=400)


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
            return JsonResponse({"result": "BOOKED"})
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
