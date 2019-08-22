from rest_framework import serializers

from .models import Car, CarModel, CarMake

class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ['id', 'name']

class CarMakeSerializer(serializers.ModelSerializer):
    models = CarModelSerializer(many=True, read_only=True)

    class Meta:
        model = CarMake
        fields = ['key','name', 'models']