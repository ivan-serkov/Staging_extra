from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.db import models
from django.urls import reverse


def get_sorted_slice(input_dict: dict, quantity=10, reverse=True):
    if input_dict:
        sorted_dict = dict(sorted(input_dict.items(), key=lambda x: x[1], reverse=reverse))
        if len(list(sorted_dict.keys())) > quantity:
            sorted_slice = {key: sorted_dict[key] for key in list(sorted_dict.keys())[:quantity]}
        else:
            sorted_slice = sorted_dict
        return sorted_slice


class Meal(models.Model):
    name = models.CharField('Название блюда', max_length=100)
    description = models.TextField('Описание блюда')
    price = models.IntegerField('Стоимость блюда')
    size = models.IntegerField('Граммовка блюда')

    def __str__(self):
        return self.name

    class MealType(models.TextChoices):
        HOT_MEALS = 'Горячие блюда'
        DRINK = 'Напитки'
        DESSERT = 'Десерты'
        NO_TYPE = 'NO_TYPE'

    meal_type = models.CharField(
        max_length=100,
        choices=MealType.choices,
        default=MealType.NO_TYPE
    )


class MealImage(models.Model):
    image = models.ImageField(upload_to='meal_images/%Y/%m/%d/')
    meal = models.ForeignKey(Meal, related_name='images', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse(
            'cafe_core_app:meal',
            # kwargs={'pk': self.pk}
        )


class MealClick(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.DO_NOTHING)
    click_date = models.DateTimeField('Дата клика')
    session = models.CharField('Имя сессии', max_length=254, blank=True, null=True)
    user = models.CharField('Пользователь', max_length=254, blank=True, null=True)

    def top_clickers(meal_id=None, quantity=10):
        # Фильтруем, если есть id
        if meal_id:
            raw_clicks = MealClick.objects.filter(meal_id=meal_id)
            # Тянем словарь с пользователями
            raw_users = set(raw_clicks.values_list('user', flat=True))
            users = {user: len(raw_clicks.filter(user=user)) for user in raw_users}
            return get_sorted_slice(users, quantity, True)

    def top_meals(quantity=10):
        raw_meals = set(MealClick.objects.values_list('meal_id', flat=True))
        meals = {meal: len(list(MealClick.objects.filter(meal_id=meal))) for meal in raw_meals}
        return get_sorted_slice(meals, quantity, True)
