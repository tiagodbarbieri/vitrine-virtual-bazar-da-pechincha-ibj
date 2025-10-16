from django.contrib.auth.models import User
from django.test import TestCase
from unittest.mock import patch
from users.models import UserInfo
from users.forms import Register, Update


class TestarRegister(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="maria",
            password="maria@9874#",
            email="maria.silva@gmail.com",
        )
        self.user_info = UserInfo.objects.create(
            cpf="754.896.384-00",
            birthday="1980-02-01",
            gender="F",
            phone_number="(11)91234-5678",
            privacy_police=True,
            user=self.user,
        )

    @patch("users.forms.ReCaptchaField.clean")
    def testar_criacao_de_usuario_valido(self, mock_clean):
        mock_clean.return_value = None  # Simula CAPTCHA válido

        dados = {
            "username": "joao",
            "email": "joao.silva@gmail.com",
            "password": "joao@9874#",
            "password_confirmation": "joao@9874#",
            "first_name": "Joao",
            "last_name": "Silva",
            "cpf": "092.274.019-46",
            "birthday": "1980-02-01",
            "phone_number": "(11)91234-5678",
            "gender": "M",
            "privacy_police": "on",
            "g-recaptcha-response": "fake-response",
        }
        form = Register(data=dados)
        self.assertTrue(form.is_valid())

    @patch("users.forms.ReCaptchaField.clean")
    def testar_criacao_de_usuario_invalido(self, mock_clean):
        mock_clean.return_value = None  # Simula CAPTCHA válido

        dados = {
            "username": "maria",
            "email": "maria.silva@gmail.com",
            "password": "maria@9874#",
            "password_confirmation": "maria@9874",
            "first_name": "Maria",
            "last_name": "Silva",
            "cpf": "754.896.384-00",
            "birthday": "1980-02-01",
            "phone_number": "(11)91234-56781",
            "gender": "F",
            "privacy_police": "on",
            "g-recaptcha-response": "fake-response",
        }
        form = Register(data=dados)
        self.assertFalse(form.is_valid())
        self.assertIn('O nome de usuário "maria" já está cadastrado!', form.errors["username"])
        self.assertIn('O e-mail "maria.silva@gmail.com" já está cadastrado!', form.errors["email"])
        self.assertIn("As senhas digitadas não coincidem!", form.errors["password_confirmation"])
        self.assertIn("Esse CPF já está cadastrado!", form.errors["cpf"])
        self.assertIn("O número de celular informado é invalido! informe o DDD + número.", form.errors["phone_number"])


class TestarUpdate(TestCase):
    def setUp(self):
        self.user_01 = User.objects.create_user(
            username="maria",
            password="maria@9874#",
            email="maria.silva@gmail.com",
        )
        self.user_info = UserInfo.objects.create(
            cpf="754.896.384-00",
            birthday="1980-02-01",
            gender="F",
            phone_number="(11)91234-5678",
            privacy_police=True,
            user=self.user_01,
        )
        self.user_02 = User.objects.create_user(
            username="joao",
            password="joao@9874#",
            email="joao.silva@gmail.com",
        )
        self.user_info_02 = UserInfo.objects.create(
            cpf="092.274.019-46",
            birthday="1980-02-01",
            gender="M",
            phone_number="(11)91234-5678",
            privacy_police=True,
            user=self.user_02,
        )

    def testar_atualizacao_de_dados_validos(self):
        dados = {
            "username": "mariazinha",  # atualizando username
            "email": "mariazinha.silva@gmail.com",  # atualizando e-mail
            "password": "maria@9874#",
            "password_confirmation": "maria@9874#",
            "first_name": "Maria",
            "last_name": "Silva",
            "cpf": "754.896.384-00",
            "birthday": "1985-03-15",  # atualizando data de aniversário
            "phone_number": "(11)91234-1000",  # atualizando celular
            "gender": "F",
            "privacy_police": "on",
        }
        form = Update(user_logged=self.user_01, data=dados)
        self.assertTrue(form.is_valid())

    # Usuário 01 tentando atualizar com dados existentes no usuário 02
    def testar_atualizacao_de_dados_invalidos(self):
        dados = {
            "username": "joao",
            "email": "joao.silva@gmail.com",
            "password": "joao@9874#",
            "password_confirmation": "joao@9874",
            "first_name": "Joao",
            "last_name": "Silva",
            "cpf": "092.274.019-46",
            "birthday": "1980-02-01",
            "phone_number": "(11)91234-56781",
            "gender": "M",
            "privacy_police": "on",
        }
        form = Update(user_logged=self.user_01, data=dados)
        self.assertFalse(form.is_valid())
        self.assertIn('O nome de usuário "joao" já está cadastrado!', form.errors["username"])
        self.assertIn('O e-mail "joao.silva@gmail.com" já está cadastrado!', form.errors["email"])
        self.assertIn("As senhas digitadas não coincidem!", form.errors["password_confirmation"])
        self.assertIn("Esse CPF já está cadastrado!", form.errors["cpf"])
        self.assertIn("O número de celular informado é invalido! informe o DDD + número.", form.errors["phone_number"])
