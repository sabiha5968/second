from rest_framework import serializers
from .models import DRF

class DRF_serializer(serializers.ModelSerializer):
    class Meta:
        model=DRF
        fields= '__all__'


