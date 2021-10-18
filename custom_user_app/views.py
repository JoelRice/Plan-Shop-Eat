from django.shortcuts import HttpResponseRedirect, reverse, render
from django.contrib.auth.decorators import login_required
from custom_user_app.models import CustomUser

@login_required
def user_profile_view(request, user_id):
    template_name = "user_profile.html"
    user_profile = CustomUser.objects.get(id=user_id)
    user_favortied_recipes = user_profile.recipe_favorited_by.all()
    users_recipes = user_profile.recipe_custom_user.all()
    users_meal_plans = user_profile.meal_plan_created_by.all()
    return render(
        request, 
        template_name,
        {
        "user_profile": user_profile, 
        "user_favortied_recipes": user_favortied_recipes,
        "users_recipes": users_recipes,
        "users_meal_plans": users_meal_plans
        }
        )

def css_mode_view(request, id):
    if request.user.id != id:
        return HttpResponseRedirect(
            request.META.get('HTTP_REFERER'),
            reverse('recipes')
            )
    if request.user.isDarkMode:
        request.user.isDarkMode = False
    else:
        request.user.isDarkMode = True
    request.user.save()
    return HttpResponseRedirect(
        request.META.get('HTTP_REFERER'),
        reverse('recipes')
        )