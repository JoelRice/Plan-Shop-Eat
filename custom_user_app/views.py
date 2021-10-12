from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from custom_user_app.models import CustomUser
from meal_plan_app.models import MealPlan

@login_required
# recipe_custom_user is the related name for created_by
def user_profile_view(request, user_id):
    template_name = "user_profile.html"
    user_profile = CustomUser.objects.get(id=user_id)
    user_favortied_recipes = user_profile.recipe_favorited_by.all()
    users_recipes = user_profile.recipe_custom_user.all()
    return render(
        request, 
        template_name,
        {
        "user_profile": user_profile, 
        "user_favortied_recipes": user_favortied_recipes,
        "users_recipes": users_recipes
        }
        )


# def users_meal_plan(request):
#     template_name = "user_profile.html"
#     plans = MealPlan.objects.all()
#     return render(
#         request, 
#         template_name,
#         {"plans": plans})