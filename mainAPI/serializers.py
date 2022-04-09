from rest_framework import serializers
from . models import vehicls

class vehiclsSerializer(serializers.Hyperlink):
    class meta:
        model = vehicls
        fields = ('name', 'description')
    