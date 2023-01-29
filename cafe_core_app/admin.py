from django.contrib import admin
from .models import *


class MealAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'meal_type', 'name', 'price', 'size',
    ]
    list_display_links = [
        'id', 'meal_type', 'name',
    ]


class MealImageAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'meal', 'image',
    ]
    list_display_links = [
        'id', 'meal',
    ]


admin.site.register(Meal, MealAdmin)
admin.site.register(MealImage, MealImageAdmin)
