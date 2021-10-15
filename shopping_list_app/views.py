from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, reverse
from django.views.generic import View
from custom_user_app.models import CustomUser
from meal_plan_app.models import MealPlan




# Create your views here.
class ShoppingListsView(View):
    template_name = "shopping_lists.html"
    
    def get(self, request):
        if not request.user.id:
            return HttpResponseRedirect(reverse("login"))
        user = CustomUser.objects.get(id=request.user.id)
        meal_plans = MealPlan.objects.filter(created_by=user)
        context = {'meal_plans': meal_plans, 'user': user}
        return render(request, self.template_name, context)

@login_required
def shopping_list_view(request, id):
    template_name = "shopping_list.html"
    meal_plan = MealPlan.objects.get(id=id)
    ingredients = meal_plan.shopping_list['ingredients']
    tools = meal_plan.shopping_list['tools']
    displayname = meal_plan.created_by.displayname
    context = {
        'ingredients': ingredients, 
        'displayname': displayname, 
        'tools': tools
        }
    return render(request, template_name, context)

