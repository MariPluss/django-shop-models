from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import RegisterForm


# 🔹 РЕГИСТРАЦИЯ
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegisterForm()

    return render(request, "accounts/register.html", {"form": form})


# 🔹 ВХОД
class CustomLoginView(LoginView):
    template_name = "accounts/login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("profile")


# 🔹 ВЫХОД (через ссылку)
def logout_view(request):
    logout(request)
    return redirect("login")


# 🔹 ПРОФИЛЬ (только для авторизованных)
@login_required
def profile_view(request):
    return render(request, "accounts/profile.html")
