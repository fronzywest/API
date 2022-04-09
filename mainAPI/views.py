from django.shortcuts import render
from rest_framework import viewsets
from . serializers import vehiclsSerializer
from . models import vehicls

class vehiclviewset(viewsets.ModelViewset):
    query = vehicls.object.all().order_by('name')
    serializer_class = vehiclsSerializer
