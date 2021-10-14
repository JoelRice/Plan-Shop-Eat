from django.urls import path, include

from meal_plan_app.views import CreateMealPlanView, EditMealPlanView, meal_plan_view, meal_plans_list_view


urlpatterns = [
    path('meal_plan/<int:id>/', meal_plan_view, name='meal_plan_view'),
    path('meal_plans/', meal_plans_list_view, name='meal_plans_view'),
    path('create_meal_plan/', CreateMealPlanView.as_view(), name="create_meal_plan"),
    path('edit_meal_plan/<int:id>/', EditMealPlanView.as_view(), name="edit_meal_plan"),
]