from django.test import TestCase
from users.views import cadastro
from users.views import redefinir_senha
from users.views import minha_conta
from users.views import minhas_reservas
from users.views import reservar_item
from users.views import apagar_reserva
from users.views import login
from users.views import logout
from users.views import excluir_conta


class TestarPaginaCadastro(TestCase):
    def testar_se_cadastro_carrega_completamente(self):
        pass

    def testar_se_o_cadastro_tem_sucesso(self):
        pass


class TestarPaginaRedefinirSenha(TestCase):
    def testar_se_redefinir_senha_carrega_completamente(self):
        pass


class TestarPaginaMinhaConta(TestCase):
    def testar_se_minha_conta_carrega_completamente(self):
        pass

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
