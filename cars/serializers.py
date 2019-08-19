from rest_framework import serializers

from .models import Car, CarModel, CarMake

class CarMakeSerializer(serializers.ModelSerializer):
    models = serializers.StringRelatedField(many=True)

    class Meta:
        model = CarMake
        fields = ['name', 'models']