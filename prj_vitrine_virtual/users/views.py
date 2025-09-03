from django.shortcuts import render


def cadastro(request):
    return render(request, "cadastro.html")


def redefinir_senha(request):
    return render(request, "redefinir_senha.html")


def minha_conta(request):
    return render(request, "minha_conta.html")


def minhas_reservas(request):
    return render(request, "minhas_reservas.html")


def logout(request):
    return render(request, "logout.html")
