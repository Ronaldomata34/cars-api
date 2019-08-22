from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from .models import CarMake
from .serializers import CarMakeSerializer

# Create your views here.
class CarMakeFilterView(generics.ListAPIView):
    serializer_class = CarMakeSerializer

    def get_queryset(self):
        if not self.request.query_params:
            return CarMake.objects.all()
        key_make = self.request.query_params.get('keymake')
        if key_make:
            queryset = CarMake.objects.filter(key__iexact=key_make)
        else:
            queryset = CarMake.objects.none()

        return queryset
