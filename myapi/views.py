from django.shortcuts import render
from rest_framework import generics, viewsets, filters, views
from rest_framework.response import Response
from .serializers import LoactionSerializer, LandmarkSerializer
from .models import Locations, Landmarks
from django_filters.rest_framework import DjangoFilterBackend


class LocationsViewSet(viewsets.ModelViewSet):
    serializer_class = LoactionSerializer
    queryset = Locations.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['country', 'city', 'id']
    ordering_fields = ['country', 'city', 'id']


class LandmarkViewSet(viewsets.ModelViewSet):
    serializer_class = LandmarkSerializer
    queryset = Landmarks.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['landmark', 'id']
    ordering_fields = ['landmark', 'id']

class LandmarksbyLocation(views.APIView):
    def get(self, request, *args, **kwargs):
        location_id = list(kwargs.values())[0]
        queryset = Landmarks.objects.filter(city_id=location_id)
        serializer = LandmarkSerializer(queryset, many=True)
        return Response(serializer.data)

# Create your views here.
