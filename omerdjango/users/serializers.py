from rest_framework import serializers

from .models import DataPoint
from .models import Fruit


class DataPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataPoint
        fields = ["label", "value"]




class FruitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fruit
        fields = ['name', 'calories']