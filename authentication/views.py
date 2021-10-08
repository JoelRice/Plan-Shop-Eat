from django.shortcuts import render, HttpResponseRedirect, reverse
from custom_user_app.forms import CustomUserCreationForm
from authentication.forms import LoginForm
from django.contrib.auth import login, authenticate, logout
from custom_user_app.models import CustomUser
# Create your views here.

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get(
                "username"), password=data.get("password"))
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse("homepage"))
    form = LoginForm()
    return render(request, "generic_form.html", {"form": form})


def signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = CustomUser.objects.create_user(
                username=data['username'],
                displayname=data['displayname'],
                password=data['password'], 
                )
        return HttpResponseRedirect(reverse('homepage'))
    form = CustomUserCreationForm()
    return render(request, 'generic_form.html', {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))