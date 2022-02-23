from django.shortcuts import render

from wsgiref.util import FileWrapper
from .custom_renderers import JPEGRenderer, PNGRenderer
from rest_framework import generics
from services.models import ServicesPictures,Packages
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import renderers
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.decorators import renderer_classes, api_view
from rest_framework.renderers import StaticHTMLRenderer
from django.http import HttpResponse
from PIL import Image
from . import serializers

class ImageAPIViewSingel(generics.RetrieveAPIView):
    renderer_classes = [JPEGRenderer,PNGRenderer]

    def get(self, request, *args, **kwargs):
        print(request.data)
        queryset = ServicesPictures.objects.get(id=self.kwargs['id']).image
        data = queryset
        print(data)
        return Response(data, content_type='image/jpg')

class ImageView(APIView):
    def get(self,request):
        images = ServicesPictures.objects.order_by('id')
        serializer = serializers.PicturesSerializer(images,many=True)
        return Response({'images': serializer.data})

class PackagesView(APIView):
    def get(self,request,sv_id):
        packges = Packages.objects.all()
        packges = packges.filter(sv_id=sv_id)
        serializer = serializers.PackagesSerializer(packges, many=True)
        return Response({'packages': serializer.data})


