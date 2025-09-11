from django import forms

# from django.contrib.auth.models import User
# from users.models import UserInfo

GENDER = [("M", "Masculino"), ("F", "Feminino"), ("O", "Outro")]


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

    # Acrescentar métodos de validação e alerta de erros
