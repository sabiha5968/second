from django.shortcuts import render
from rest_framework import generics   #generic class will provide web brousable APIs
from .models import DRF
from .serializer import DRF_serializer


class API_objects(generics.ListCreateAPIView):
    queryset=DRF.objects.all()
    serializer_class=DRF_serializer

class object_details(generics.RetrieveUpdateDestroyAPIView):
    queryset=DRF.objects.all()
    serializer_class= DRF_serializer

# Create your views here.
