from django.shortcuts import render
from rest_framework import viewsets
from .serializers import LoactionsSerializer
from .models import Locations


class LocationsViewSet(viewsets.ModelViewSet):
    queryset = Locations.objects.all().order_by("city")
    serializer_class = LoactionsSerializer

# Create your views here.
