from django.urls import path
from users.views import cadastro
from users.views import redefinir_senha
from users.views import minha_conta
from users.views import minhas_reservas
from users.views import reservar_item
from users.views import apagar_reserva
from users.views import login
from users.views import logout
from users.views import excluir_conta


urlpatterns = [
    path("cadastro/", cadastro, name="home-page"),
    path("redefinir-senha/", redefinir_senha, name="redefinir-senha"),
    path("minha-conta/", minha_conta, name="minha-conta"),
    path("minhas-reservas/", minhas_reservas, name="minhas-reservas"),
    path("reservar-item/", reservar_item, name="reservar-item"),
    path("apagar-reserva/", apagar_reserva, name="apagar-reserva"),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("excluir-conta/", excluir_conta, name="excluir-conta"),
]
