from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import *
from .models import *


class SohaAPI(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            sohalar = Soha.objects.all()
            serializer = SohaSerializer(sohalar, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return status.HTTP_407_PROXY_AUTHENTICATION_REQUIRED


class SavollarAPI(APIView):
    def get(self, request, pk):
        savollar = Savollar.objects.filter(id=pk)
        serializer = SavollarSerializer(savollar, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)