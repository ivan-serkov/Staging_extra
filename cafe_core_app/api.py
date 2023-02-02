from .models import *
from rest_framework import viewsets, permissions
from .serializers import *


class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MealSerializer


class MealClickViewSet(viewsets.ModelViewSet):
    queryset = MealClick.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MealClickSerializer


class MealImageViewSet(viewsets.ModelViewSet):
    queryset = MealImage.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MealImageSerializer
