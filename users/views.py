from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
import stripe
from rest_framework.response import Response
from users.models import UserProfile, Appointments, Feedback
from django.shortcuts import redirect
from users.serializers import UserLoginSerializer, UserProfileSerializer, AppointmentSerializer, FeedSerializer
from rest_framework import status, viewsets
import jwt, datetime
from django.conf import settings
from rest_framework.views import APIView


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
                token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256').decode('utf-8')
                return JsonResponse({'jwt': token}, status=200)
                # return JsonResponse({'result': "1", 'message': "login successful", "user_id": user.id})
        except UserProfile.DoesNotExist:
            return JsonResponse({'result': "2", 'message': "the email or password is not correct"}, status=400)

    return JsonResponse({'result': "failed "}, status=400)


@api_view(['PUT'])
#@permission_classes([IsAuthenticated])
def EditProfile(request, id):
    if request.method == 'PUT':
        user = UserProfile.objects.get(id=id)
        serializer = UserProfileSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)


@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def GetSpecificUser(request, id):
    if request.method == 'GET':
        user = UserProfile.objects.get(id=id)
        if user:
            user2 = {"phone": user.phone,
                     "First_Name": user.First_Name,
                     "Last_Name": user.Last_Name,
                     "birth": user.birth,
                     "email": user.email,
                     "password": user.password,
                     "address": user.address}
            return JsonResponse(user2)
        return JsonResponse({"result": "Didn't Find The User"}, status=400)


#@permission_classes([IsAuthenticated])
class GetAppointement(viewsets.ModelViewSet):
    queryset = Appointments.objects.all()
    serializer_class = AppointmentSerializer



@api_view(['POST'])
#@permission_classes([IsAuthenticated])
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

stripe.api_key = settings.STRIPE_SECRET_KEY

class StripeCheckoutView(APIView):
    def post(self,request):
        print(1)
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                        'price': 'price_1KYuYFFVwpm3iA1up22JDeue',
                        'quantity': 1,
                    },
                ],
                payment_method_types=['card',],
                mode='payment',
                success_url= settings.SITE_URL + '/?success=true&session_id={CHECKOUT_SESSION_ID}',
                cancel_url=settings.SITE_URL + '/?canceled=true',
            )
            print(2)
            return redirect(checkout_session.url)

        except:
            return Response(
                {'error': 'Something went wrong when creating stripe checkout session'},
                status= status.HTTP_500_INTERNAL_SERVER_ERROR
            )