from rest_framework import serializers
from .models import *


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = '__all__'


class MealClickSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealClick
        fields = '__all__'

class MealImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealImage
        fields ='__all__'
