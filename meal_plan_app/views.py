from django.shortcuts import render
from . models import MealPlan
# Create your views here.


def meal_plan_view(request, id):
    meal = MealPlan.objects.get(id=id)
    return render(request, 'meal_plan.html', {'meal':meal})


def plan(request):
    plans = MealPlan.objects.all()
    return render(request, 'plans.html', {'plans': plans})