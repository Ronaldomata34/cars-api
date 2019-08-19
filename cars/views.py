from django.shortcuts import render

from rest_framework import viewsets

from .models import CarMake
from .serializers import CarMakeSerializer

# Create your views here.
class CarMakeViewSet(viewsets.ModelViewSet):
    queryset = CarMake.objects.all()
    serializer_class = CarMakeSerializer
    #permission_classes = [IsAccountAdminOrReadOnly]