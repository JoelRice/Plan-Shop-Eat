from django.shortcuts import render, HttpResponseRedirect, reverse
from authentication.forms import LoginForm, SignUpForm
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import login, authenticate, logout
from custom_user_app.models import CustomUser
# Create your views here.

# change Http redirect!!!
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get(
                "username"), password=data.get("password"))
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse("recipes"))
            else:
                return render(
                    request,
                    "generic_form.html",
                    {
                        "form": form,
                        'form_title': 'Log In',
                        'error_message': 'Username or Password were invalid...'
                        }
                    )
    form = LoginForm()
    return render(request, "generic_form.html", {"form": form, 'form_title': 'Log In'})

# change Http redirect!!!
def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if CustomUser.objects.filter(username=data['username']).exists():
                return render(
                    request,
                    'generic_form.html',
                    {
                        "form": form,
                        'form_title': 'Sign Up',
                        'error_message': 'Username already exists...'
                        }
                    )
            isValid = True
            try:
                validate_password(data['password'])
            except:
                isValid = False
            if not isValid:
                return render(
                    request,
                    'generic_form.html',
                    {
                        "form": form,
                        'form_title': 'Sign Up',
                        'error_message': "That password ain't right"
                        }
                    )
                
            user = CustomUser.objects.create_user(
                username=data['username'],
                displayname=data['displayname'],
                password=data['password'],
                )
        return HttpResponseRedirect(reverse('recipes'))
    form = SignUpForm()
    return render(request, 'generic_form.html', {"form": form, 'form_title': 'Sign Up'})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))