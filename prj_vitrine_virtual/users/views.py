from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout
from django.contrib.auth import login as django_login
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required


def cadastro(request):
    return render(request, "cadastro.html")


def redefinir_senha(request):
    return render(request, "redefinir_senha.html")


@login_required
def minha_conta(request):
    return render(request, "minha_conta.html")


@login_required
def minhas_reservas(request):
    return render(request, "minhas_reservas.html")


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            django_login(request, user)
            return JsonResponse({"success": True})
        else:
            return JsonResponse({"success": False})
    else:
        return redirect("/")


@login_required
def logout(request):
    user_first_name = request.user.first_name
    django_logout(request)
    return render(request, "logout.html", {"user_first_name": user_first_name})
