from django import forms
from users.models import GENDER
from users.models import UserInfo
from django.contrib.auth.models import User


class Register(forms.Form):
    username = forms.CharField(
        label="Nome de usuário",
        max_length=150,
        widget=forms.TextInput(attrs={"class": "form-control mb-3", "placeholder": "Ex: joaosilva"}),
    )
    email = forms.EmailField(
        label="E-mail",
        widget=forms.EmailInput(attrs={"class": "form-control mb-3", "placeholder": "exemplo@dominio.com"}),
    )
    password = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(attrs={"class": "form-control mb-3"}),
    )
    password_confirmation = forms.CharField(
        label="Confirme a senha",
        widget=forms.PasswordInput(attrs={"class": "form-control mb-3"}),
    )
    first_name = forms.CharField(
        label="Primeiro nome",
        max_length=150,
        widget=forms.TextInput(attrs={"class": "form-control mb-3", "placeholder": "Ex: João"}),
    )
    last_name = forms.CharField(
        label="Segundo nome",
        max_length=150,
        widget=forms.TextInput(attrs={"class": "form-control mb-3", "placeholder": "Ex: da Silva"}),
    )
    cpf = forms.CharField(
        label="CPF",
        max_length=14,
        widget=forms.TextInput(attrs={"class": "form-control mb-3", "placeholder": "Somente números"}),
    )
    birthday = forms.DateField(
        label="Data de nascimento",
        widget=forms.DateInput(attrs={"type": "date", "class": "form-control mb-3"}),
    )
    phone_number = forms.CharField(
        label="Celular",
        max_length=20,
        widget=forms.TextInput(attrs={"class": "form-control mb-3", "placeholder": "DDD + número"}),
    )
    gender = forms.ChoiceField(
        label="Gênero",
        choices=GENDER,
        widget=forms.Select(attrs={"class": "form-control mb-3"}),
    )
    privacy_police = forms.BooleanField(
        label="Aceito a Política de Privacidade.",
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"}),
    )

    # Métodos de validação e alerta de erros

    # Verificar se o nome do usuário já está cadastrado
    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username__contains=username):
            raise forms.ValidationError(f'O nome de usuário "{username}" já existe!')
        return username

    # Verificar se o e-mail já está cadastrado
    # Verificar se o password está forte
    # Verificar se o password e a confirmação estão iguais
    # Verificar se o CPF está correto
    # Verificar se o número de telefone está correto
