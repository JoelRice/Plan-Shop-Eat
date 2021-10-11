from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from custom_user_app.models import CustomUser
from recipe_app.models import Recipe

@login_required
def user_profile_view(request, user_id):
    user_profile = CustomUser.objects.get(id=user_id)
    user_favortied_recipes = user_profile.recipe_favorited_by.all()
    return render(request, "user_profile.html",{"user_profile": user_profile, "user_favortied_recipes": user_favortied_recipes})
    

# def users_fav_recipe_view(request):
#     favorites = request.user.favorited_by.all()
#     user_favortied_recipes = list(favorites)
#     return render(request, "user_profile.html",{"user_favortied_recipes": user_favortied_recipes})