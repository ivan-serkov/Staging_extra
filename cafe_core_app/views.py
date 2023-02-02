from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Meal, MealClick, MealImage
from django.utils import timezone


def menu(request):
    meal_categories = list(filter(lambda el: 'NO_TYPE' not in el[0], Meal.MealType.choices))
    context = {
        'meal_categories': meal_categories,
        'title': 'Меню',
    }
    return render(request, 'cafe_core_app/menu.html', context)


def meal_category(request, meal_category):
    meals_by_category = Meal.objects.filter(meal_type=meal_category)
    context = {
        'meals': meals_by_category,
        'meal_category': meal_category,
        'title': meal_category
    }
    return render(request, 'cafe_core_app/meals.html', context)


def meal(request, meal_id):
    meal = Meal.objects.get(id=meal_id)
    if request.user.is_authenticated:
        meal.mealclick_set.create(click_date=timezone.now(), user=request.user.username,
                                  session=request.session.session_key)
    else:
        meal.mealclick_set.create(click_date=timezone.now(), session=request.session.session_key)
    context = {
        'meal': meal,
        'meal_category': meal.meal_type,
        'images': MealImage.objects.filter(meal=meal_id)
    }
    return render(request, 'cafe_core_app/meal.html', context)


def meal_statistics(request):
    context = {
        'top_meals': MealClick.top_meals(10),
        'users': User.objects.all(),
        'meal': Meal.objects.all(),
    }
    # print(context['top_meals'].items())
    return render(request, 'cafe_core_app/statistics.html', context)


def stats(request, meal_id):
    top_ten_clickers = MealClick.top_clickers(meal_id, 10)
    clicks = MealClick.objects.filter(meal_id=meal_id).values('click_date')
    # print(clicks)
    context = {
        'top_ten_clickers': top_ten_clickers,
        'stats': MealClick.objects.filter(meal_id=meal_id),
        'serie': MealClick.objects.filter(meal_id=meal_id).values(),
        'meal': Meal.objects.get(id=meal_id)
    }
    return render(request, 'cafe_core_app/stats.html', context)
