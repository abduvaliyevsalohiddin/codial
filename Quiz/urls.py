from django.contrib import admin
from django.urls import path
from mainApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('soha/', SohaAPI.as_view()),
    path('soha_savol/<int:pk>/', SavollarAPI.as_view()),
]
