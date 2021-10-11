from django.urls import path, include

# from . import views
from meal_plan_app.views import meal_plan_view, plan
from django.conf.urls import include, url



urlpatterns = [
    path('meal_plan/<int:id>/', meal_plan_view, name='meal_plan_view'),
    path('plan/', plan, name='plan'),
]