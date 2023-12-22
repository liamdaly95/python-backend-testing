from rest_framework import serializers

from .models import Locations, Landmarks

class LoactionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Locations
        fields = ['id', 'city', 'country']

class LandmarkSerializer(serializers.HyperlinkedModelSerializer):
    city_name = serializers.CharField(source='city.city')
    country_name = serializers.CharField(source='city.country')
    city_id = serializers.CharField(source='city.id')
    class Meta:
        model = Landmarks
        fields = ['id', 'landmark', 'city_name', 'country_name', 'city_id']

