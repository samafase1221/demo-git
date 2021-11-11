from django.shortcuts import render
from rest_framework import generics
from .serializers import PersonaSoporteSerializer
from .models import PersonaSoporte
from .serializers import PQRSerializer
from .models import PQR


# Create your views here.

class PersonaSoporteListCreate(generics.ListCreateAPIView):
    queryset = PersonaSoporte.objects.all()
    serializer_class = PersonaSoporteSerializer

    
class PersonaSoporteUpdateDelete(generics.RetriveUpdateDeleteAPIView):
    queryset = PersonaSoporte.objects.all()
    serializer_class = PersonaSoporteSerializer

class PQRListCreate(generics.ListCreateAPIView):
    queryset = PQR.objects.all()
    serializer_class = PQRSerializer

    
class PQRUpdateDelete(generics.RetriveUpdateDeleteAPIView):
    queryset = PQR.objects.all()
    serializer_class = PQRSerializer
