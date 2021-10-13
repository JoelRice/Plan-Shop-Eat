from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, reverse
from django.views.generic import View, CreateView, FormView
from custom_user_app.models import CustomUser
from meal_plan_app.models import MealPlan
from recipe_app.models import Recipe, Tool, Ingredient, Review
from shopping_list_app.models import ShoppingList


# Create your views here.
class ShoppingListsView(View):
    template_name = "shopping_lists.html"
    
    def get(self, request):
        if not request.user.id:
            return HttpResponseRedirect(reverse("login"))
        user = CustomUser.objects.get(id=request.user.id)
        meal_plans = MealPlan.objects.filter(created_by=user)
        shopping_lists = ShoppingList.objects.filter(meal_plan__in=meal_plans)
        context = {'shopping_lists': shopping_lists, 'meal_plans': meal_plans, 'user': user}
        return render(request, self.template_name, context)


def shopping_list_view(request, slid):
    if not request.user.id:
        return HttpResponseRedirect(reverse("login"))
    template_name = "shopping_list.html"
    user = CustomUser.objects.get(id=request.user.id)
    shopping_list = ShoppingList.objects.get(id=slid)
    tools = shopping_list.tools.all()
    ingredients = shopping_list.ingredients.all()
    context = {'user': user, 'shopping_list': shopping_list, 'tools': tools, 'ingredients': ingredients }
    return render(request, template_name, context)

