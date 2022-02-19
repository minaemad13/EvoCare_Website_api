
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from users.models import UserProfile

from users.serializers import UserLoginSerializer, UserProfileSerializer

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
        user = UserProfile.objects.get(email=email, password=password)

        if user:
            return JsonResponse({'result': "Login", "user_id": user.id
                                 })
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
