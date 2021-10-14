from django.shortcuts import render, reverse, HttpResponseRedirect
from django.views import View
from meal_plan_app.forms import CreateMealPlanForm
from meal_plan_app.models import MealPlan
# Create your views here.


def meal_plan_view(request, id):
    meal = MealPlan.objects.get(id=id)
    return render(request, 'meal_plan.html', {'meal':meal})


def meal_plans_list_view(request):
    plans = MealPlan.objects.all()
    return render(request, 'meal_plans.html', {'plans': plans})

class CreateMealPlanView(View):
    template_name = 'generic_form.html'
    form = CreateMealPlanForm()

    def get(self, request):
        return render(
            request,
            self.template_name,
            {'form': self.form}
        )

    def post(self, request):
        form = CreateMealPlanForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = request.user
            meal_plan = MealPlan.objects.create(
                created_by = user,
                plan_title = data.get('plan_title')
            )
            meal_plan.monday.set(data.get('monday'))
            meal_plan.tuesday.set(data.get('tuesday'))
            meal_plan.wednesday.set(data.get('wednesday'))
            meal_plan.thursday.set(data.get('thursday'))
            meal_plan.friday.set(data.get('friday'))
            meal_plan.saturday.set(data.get('saturday'))
            meal_plan.sunday.set(data.get('sunday'))
            return HttpResponseRedirect(
                reverse('meal_plan_view', args=(meal_plan.id,))
            )

class EditMealPlanView(View):
    template_name = 'generic_form.html'
    form = CreateMealPlanForm()

    def get(self, request, id):
        meal_plan = MealPlan.objects.get(id=id)
        if not request.user == meal_plan.created_by and not request.user.is_staff:
            return HttpResponseRedirect(
                reverse('meal_plan_view', args=(meal_plan.id,))
            )
        form = CreateMealPlanForm({
            'plan_title': meal_plan.plan_title,
            'monday': meal_plan.monday.all(),
            'tuesday': meal_plan.tuesday.all(),
            'wednesday': meal_plan.wednesday.all(),
            'thursday': meal_plan.thursday.all(),
            'friday': meal_plan.friday.all(),
            'saturday': meal_plan.saturday.all(),
            'sunday': meal_plan.sunday.all(),
        })
        return render(
            request,
            self.template_name,
            {'form': form}
        )

    def post(self, request, id):
        meal_plan = MealPlan.objects.get(id=id)
        if not request.user == meal_plan.created_by and not request.user.is_staff:
            return HttpResponseRedirect(
                reverse('meal_plan_view', args=(meal_plan.id,))
            )
        form = CreateMealPlanForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            meal_plan.monday.set(data.get('monday'))
            meal_plan.tuesday.set(data.get('tuesday'))
            meal_plan.wednesday.set(data.get('wednesday'))
            meal_plan.thursday.set(data.get('thursday'))
            meal_plan.friday.set(data.get('friday'))
            meal_plan.saturday.set(data.get('saturday'))
            meal_plan.sunday.set(data.get('sunday'))
            meal_plan.plan_title = data.get('plan_title')
            meal_plan.save()
        return HttpResponseRedirect(
                reverse('meal_plan_view', args=(meal_plan.id,)),
                reverse('recipes')
            )
