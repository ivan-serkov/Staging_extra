from django.contrib import admin
from django.urls import path
from . import views
from rest_framework import routers
from .api import *

app_name = 'cafe_core_app'
router = routers.DefaultRouter()
router.register('api/meal', MealViewSet, 'api_meal')
router.register('api/mealclicks', MealClickViewSet, 'api_mealclicks')
router.register('api/mealimages', MealImageViewSet, 'api_mealimages')

urlpatterns = router.urls + [
    path('menu/', views.menu, name='menu'),
    path('admin/', admin.site.urls),
    path('<meal_category>', views.meal_category, name='meal_category'),
    path('<int:meal_id>/meal', views.meal, name='meal'),
    path('meal_statistics/', views.meal_statistics, name='meal_statistics'),
    path('<int:meal_id>/stats', views.stats, name='stats'),
]
