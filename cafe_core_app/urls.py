from django.contrib import admin
from django.urls import path
from . import views

app_name = 'cafe_core_app'
urlpatterns = [
    path('', views.menu, name='menu'),
    path('admin/', admin.site.urls),
    path('<meal_category>', views.meal_category, name='meal_category'),
    path('<int:meal_id>/meal', views.meal, name='meal'),
    path('meal_statistics/', views.meal_statistics, name='meal_statistics'),
    path('<int:meal_id>/stats', views.stats, name='stats'),

]
