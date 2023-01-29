from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import *


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile.objects.create(user=user)
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("cafe_core_app:menu")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="Users/register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("cafe_core_app:menu")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="Users/login.html", context={"login_form": form})


def password_change_request(request):
    pass
    # u = User.objects.get(username=request.user)
    # if request.method == 'POST':
    #     form = ChangePasswordForm(request.POST)
    #     if form.is_valid():
    #         old_password = request.POST.get("old_password")
    #         new_pass = request.POST.get("new_password")
    #         new_pass_rep = request.POST.get("new_password_repeat")
    #         if check_password(old_password, u.password):
    #             return HttpResponse('ok')
    #         else:
    #             return HttpResponse('bad')
    # else:
    #     form = ChangePasswordForm()
    #
    # return render(request, 'login/change_password.html',
    #               {'form': form, 'user': u})


def profile_request(request, user_id):
    user = User.objects.get(pk=user_id)
    profile = Profile.objects.get(user_id=user_id)
    return render(request=request, template_name="Users/profile.html",
                  context={"user": user, 'profile': profile})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("cafe_core_app:menu")


