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


class RegisterUser(APIView):
    def post(self, request):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SavolHisoblaAPI(APIView):
    def get(self, request):
        content = {
            "xabar": "Testlar bilan ishlash men uchun ozgina bolgani uchun iltimos qolda kiritishingizni soraymiz !",
            "masalan": "{"
                       "savollar: 20,"
                       "togri: 13"
        }
        return Response(content)

    def post(self, request):
        xabar = request.data
        savollar = int(xabar["savollar"])
        togri = int(xabar["togri"])
        natija = 100 / savollar * togri
        content = {
            "savollar": savollar,
            "togrisi": togri,
            "foizda": natija
        }
        return Response(content)
