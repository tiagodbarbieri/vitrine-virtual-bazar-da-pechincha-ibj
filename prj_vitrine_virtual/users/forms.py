from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from users.models import GENDER
from users.models import UserInfo
from users.utils import only_digits
from validate_docbr import CPF  # pip install validate-docbr
from re import sub, match
from django_recaptcha.fields import ReCaptchaField  # pip install django-recaptcha
from django_recaptcha.widgets import ReCaptchaV2Checkbox


class Register(forms.Form):
    username = forms.CharField(
        label="Nome de usuário",
        max_length=150,
        widget=forms.TextInput(attrs={"class": "form-control mb-3", "placeholder": "Ex: joaosilva", "tabindex": "1"}),
    )
    email = forms.EmailField(
        label="E-mail",
        widget=forms.EmailInput(
            attrs={"class": "form-control mb-3", "placeholder": "exemplo@dominio.com", "tabindex": "2"}
        ),
    )
    password = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(attrs={"class": "form-control mb-3", "tabindex": "3"}),
    )
    password_confirmation = forms.CharField(
        label="Confirme a senha",
        widget=forms.PasswordInput(attrs={"class": "form-control mb-3", "tabindex": "4"}),
    )
    first_name = forms.CharField(
        label="Primeiro nome",
        max_length=150,
        widget=forms.TextInput(attrs={"class": "form-control mb-3", "placeholder": "Ex: João", "tabindex": "5"}),
    )
    last_name = forms.CharField(
        label="Segundo nome",
        max_length=150,
        widget=forms.TextInput(attrs={"class": "form-control mb-3", "placeholder": "Ex: da Silva", "tabindex": "6"}),
    )
    cpf = forms.CharField(
        label="CPF",
        max_length=14,
        widget=forms.TextInput(
            attrs={"class": "form-control mb-3", "placeholder": "Ex: 123.456.789-10", "tabindex": "7"}
        ),
    )
    birthday = forms.DateField(
        label="Data de nascimento",
        widget=forms.DateInput(attrs={"type": "date", "class": "form-control mb-3", "tabindex": "8"}),
    )
    phone_number = forms.CharField(
        label="Celular",
        max_length=20,
        widget=forms.TextInput(attrs={"class": "form-control mb-3", "placeholder": "DDD + número", "tabindex": "9"}),
    )
    gender = forms.ChoiceField(
        label="Gênero",
        choices=GENDER,
        widget=forms.Select(attrs={"class": "form-control mb-3", "tabindex": "10"}),
    )
    privacy_police = forms.BooleanField(
        label="Aceito a Política de Privacidade.",
        widget=forms.CheckboxInput(attrs={"class": "form-check-input", "tabindex": "11"}),
    )
    captcha = ReCaptchaField(
        widget=ReCaptchaV2Checkbox(attrs={"tabindex": "12"}),
        error_messages={"required": "Faça a verificação do reCAPTCHA!"},
    )

    # ---------------------------------------------------------------------------------------------
    # Métodos de validação e alerta de erros
    # ---------------------------------------------------------------------------------------------

    # Verificar se o nome do usuário já está cadastrado
    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username):
            raise forms.ValidationError(f'O nome de usuário "{username}" já está cadastrado!')
        return username

    # Verificar se o e-mail já está cadastrado
    def clean_email(self):
        email = self.cleaned_data.get("email")

        # Acrescentar validação de e-mail do Django

        if User.objects.filter(email=email):
            raise forms.ValidationError(f'O e-mail "{email}" já está cadastrado!')
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirmation = cleaned_data.get("password_confirmation")

        # Verificar se o password e a confirmação estão iguais
        if password != password_confirmation:
            msg = "As senhas digitadas não coincidem!"
            self.add_error("password_confirmation", msg)

        # Validando o password com as funções Django
        validate_password(str(password))

        # Retornar o cleaned_data completo (não sobrescrever com um dicionário parcial)
        return cleaned_data

    # Verificar se o CPF está correto
    def clean_cpf(self):
        cpf = only_digits(str(self.cleaned_data.get("cpf")))
        validator = CPF()
        if UserInfo.objects.filter(cpf=validator.mask(cpf)):
            raise forms.ValidationError("Esse CPF já está cadastrado!")
        if not validator.validate(cpf):
            raise forms.ValidationError("O CPF informado é inválido!")
        return cpf

    # Verificar se o número de celular está correto
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get("phone_number")
        cellphone = sub("[^0-9]", "", str(phone_number))
        if not bool(match("^([14689][0-9]|2[12478]|3([1-5]|[7-8])|5([13-5])|7[193-7])9[0-9]{8}$", cellphone)):
            raise forms.ValidationError("O número de celular informado é invalido! informe o DDD + número.")
        return phone_number


class Update(Register):
    captcha = None

    def __init__(self, *args, user_logged, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.user_logged = user_logged

    # Verificar se o nome do usuário já está cadastrado
    def clean_username(self):
        username = self.cleaned_data.get("username")
        if username == self.user_logged.username:
            return username
        if User.objects.filter(username=username):
            raise forms.ValidationError(f'O nome de usuário "{username}" já está cadastrado!')
        return username

    # Verificar se o e-mail já está cadastrado
    def clean_email(self):
        email = self.cleaned_data.get("email")

        # Acrescentar validação de e-mail do Django

        if email == self.user_logged.email:
            return email
        if User.objects.filter(email=email):
            raise forms.ValidationError(f'O e-mail "{email}" já está cadastrado!')
        return email

    # Verificar se o CPF está correto
    def clean_cpf(self):
        user_logged_cpf = UserInfo.objects.get(user=self.user_logged).cpf
        cpf = only_digits(str(self.cleaned_data.get("cpf")))
        validator = CPF()
        if validator.mask(cpf) == user_logged_cpf:
            return cpf
        if UserInfo.objects.filter(cpf=validator.mask(cpf)):
            raise forms.ValidationError("Esse CPF já está cadastrado!")
        if not validator.validate(cpf):
            raise forms.ValidationError("O CPF informado é inválido!")
        return cpf
