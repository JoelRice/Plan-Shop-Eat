from django.shortcuts import render
from meal_plan_app.models import MealPlan
# Create your views here.


def meal_plan_view(request, id):
    meal = MealPlan.objects.get(id=id)
    return render(request, 'meal_plan.html', {'meal':meal})


def meal_plans_list_view(request):
    plans = MealPlan.objects.all()
    return render(request, 'meal_plans.html', {'plans': plans})