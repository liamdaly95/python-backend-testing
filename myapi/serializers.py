from rest_framework import serializers

from .models import Locations

class LoactionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Locations
        fields = ("id", "city", "country")