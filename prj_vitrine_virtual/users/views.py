from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout
from django.contrib.auth import login as django_login
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from users.models import UserInfo
from users.forms import Register
from validate_docbr import CPF


def cadastro(request):
    if request.method == "POST":
        form = Register(request.POST)
        if form.is_valid():
            cpf_maker = CPF()

            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            cpf = form.cleaned_data["cpf"]
            birthday = form.cleaned_data["birthday"]
            phone_number = form.cleaned_data["phone_number"]
            gender = form.cleaned_data["gender"]
            privacy_police = form.cleaned_data["privacy_police"]

            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
            )

            UserInfo.objects.create(
                cpf=cpf_maker.mask(cpf),
                birthday=birthday,
                phone_number=phone_number,
                gender=gender,
                privacy_police=privacy_police,
                user=user,
            )
            return render(request, "cadastro_finalizado.html", {"user_first_name": first_name})
    else:
        form = Register()
    return render(request, "cadastro.html", {"form": form})


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
