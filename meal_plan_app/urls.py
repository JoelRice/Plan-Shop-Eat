from django.urls import path, include

from . import views
from meal_plan_app import views
from django.conf.urls import include, url


urlpatterns = [
    path('<int:id>', views.meal_plan_view, name='meal_plan_index'),
    path('plan/', views.plans_view, name='plan'),
]