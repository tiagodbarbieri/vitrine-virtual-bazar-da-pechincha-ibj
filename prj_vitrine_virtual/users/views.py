from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout
from django.contrib.auth import login as django_login
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from users.models import UserInfo
from users.forms import Register, Update
from users.utils import only_digits
from validate_docbr import CPF


def cadastro(request):
    if request.method == "POST":
        form = Register(request.POST)
        if form.is_valid():
            cpf_maker = CPF()

            username = request.POST.get("username")
            email = request.POST.get("email")
            password = request.POST.get("password")
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            cpf = request.POST.get("cpf")
            birthday = request.POST.get("birthday")
            phone_number = request.POST.get("phone_number")
            gender = request.POST.get("gender")
            privacy_police = True if (request.POST.get("privacy_police")) == "on" else False

            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
            )

            UserInfo.objects.create(
                cpf=cpf_maker.mask(only_digits(cpf)),
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
    user = User.objects.get(username=request.user.username)
    user_info = UserInfo.objects.get(user=user)

    if request.method == "POST":
        form = Update(request.POST, user_logged=request.user)
        if form.is_valid():
            cpf_maker = CPF()

            # Obtendo dados do formulário
            username = request.POST.get("username")
            email = request.POST.get("email")
            password = request.POST.get("password")
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            cpf = request.POST.get("cpf")
            birthday = request.POST.get("birthday")
            phone_number = request.POST.get("phone_number")
            gender = request.POST.get("gender")

            # Atualizando banco de dados "user"
            user.username = username
            user.email = email
            user.set_password(password)
            user.first_name = first_name
            user.last_name = last_name

            # Atualizando banco de dados "user_info"
            user_info.cpf = cpf_maker.mask(only_digits(cpf))
            user_info.birthday = birthday
            user_info.phone_number = phone_number
            user_info.gender = gender

            # Salvando as alterações
            user.save()
            user_info.save()

            return render(request, "dados_atualizados.html", {"user_first_name": first_name})
        else:
            return render(request, "minha_conta.html", {"form": form})
    else:
        # preencher form com os dados do usuário
        form = Update(
            user_logged=request.user,
            initial={
                "username": user.username,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "cpf": user_info.cpf,
                "birthday": (
                    f"{user_info.birthday.year:04d}-{user_info.birthday.month:02d}-{user_info.birthday.day:02d}"
                ),
                "phone_number": user_info.phone_number,
                "gender": user_info.gender,
                "privacy_police": user_info.privacy_police,
            },
        )

        return render(request, "minha_conta.html", {"form": form})


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


@login_required
def excluir_conta(request):
    user_first_name = request.user.first_name
    request.user.delete()
    return render(request, "conta_excluida.html", {"user_first_name": user_first_name})
