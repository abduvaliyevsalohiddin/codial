from rest_framework import serializers
from .models import *


class SohaSerializer(serializers.ModelSerializer):
    class Meta():
        model = Soha
        fields = '__all__'


class SavollarSerializer(serializers.ModelSerializer):
    class Meta():
        model = Savollar
        fields = '__all__'
