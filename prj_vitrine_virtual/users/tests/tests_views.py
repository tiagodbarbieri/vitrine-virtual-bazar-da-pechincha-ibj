from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch

from users.models import UserInfo

# from users.views import cadastro
# from users.views import redefinir_senha
# from users.views import minha_conta
# from users.views import minhas_reservas
# from users.views import reservar_item
# from users.views import apagar_reserva
# from users.views import login
# from users.views import logout
# from users.views import excluir_conta


class TestarPaginaCadastro(TestCase):
    def testar_se_cadastro_carrega_completamente(self):
        response = self.client.get(reverse("cadastro"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "cadastro.html")
        self.assertContains(response, "CADASTRO")

    @patch("users.forms.ReCaptchaField.clean")
    def testar_se_o_cadastro_tem_sucesso(self, mock_clean):
        mock_clean.return_value = None  # Simula CAPTCHA válido

        data = {
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
        response = self.client.post(reverse("cadastro"), data)  # follow=True

        self.assertEqual(response.status_code, 200)
        # Para que os testes abaixo funcionem, será necessário criar uma nova view para cadastro finalizado
        # com gerenciamento de seção --> "request.session".

        # self.assertTemplateUsed(response, "cadastro_finalizado.html")
        # self.assertContains(response, "CADASTRO FINALIZADO")
        # self.assertContains(response, "Maria")


class TestarPaginaRedefinirSenha(TestCase):
    def testar_se_redefinir_senha_carrega_completamente(self):
        response = self.client.get(reverse("redefinir-senha"))
        self.assertAlmostEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "redefinir_senha.html")
        self.assertContains(response, "REDEFINIR SENHA")


class TestarPaginaMinhaConta(TestCase):
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
        self.client.force_login(self.user)

    def testar_se_minha_conta_carrega_completamente(self):
        response = self.client.get(reverse("minha-conta"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "minha_conta.html")
        self.assertContains(response, "maria")

    def testar_se_minha_conta_atualiza_dados(self):
        pass


class TestarPaginaMinhasReservas(TestCase):
    def testar_se_minhas_reservas_carrega_completamente(self):
        pass


class TestarPaginaReservarItem(TestCase):
    def testar_reserva_de_item_carrega_completamente(self):
        pass

    def testar_nova_reserva_de_item(self):
        pass

    def testar_atualizacao_de_reserva_de_item(self):
        pass


class TestarPaginaApagarReserva(TestCase):
    def testar_se_apagar_reserva_redireciona_para_home(self):
        pass

    def testar_apagar_reserva_de_item(self):
        pass


class TestarPaginaLogin(TestCase):
    def testar_se_login_get_redireciona_para_home(self):
        pass

    def testar_login_post_usuario_valido(self):
        pass

    def testar_login_post_usuario_invalido(self):
        pass


class TestarPaginaLogout(TestCase):
    def testar_se_logout_tem_sucesso(self):
        pass


class TestarPaginaExcluirConta(TestCase):
    def testar_exclusao_de_conta(self):
        pass
