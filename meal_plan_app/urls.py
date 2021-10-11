from django.urls import path, include

from meal_plan_app.views import meal_plan_view, plan_list_view


urlpatterns = [
    path('meal_plan/<int:id>/', meal_plan_view, name='meal_plan_view'),
    path('plans/', plan_list_view, name='plans'),
]