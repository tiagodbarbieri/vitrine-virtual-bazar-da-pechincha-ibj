from django.shortcuts import render
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required


def cadastro(request):
    return render(request, "cadastro.html")


def redefinir_senha(request):
    return render(request, "redefinir_senha.html")


def minha_conta(request):
    return render(request, "minha_conta.html")


def minhas_reservas(request):
    return render(request, "minhas_reservas.html")


@login_required
def logout(request):
    user_first_name = request.user.first_name
    django_logout(request)
    return render(request, "logout.html", {"user_first_name": user_first_name})
