from django.urls import path
from users.views import cadastro
from users.views import redefinir_senha
from users.views import minha_conta
from users.views import minhas_reservas
from users.views import logout


urlpatterns = [
    path("cadastro/", cadastro, name="home-page"),
    path("redefinir-senha/", redefinir_senha, name="redefinir-senha"),
    path("minha-conta/", minha_conta, name="minha-conta"),
    path("minhas-reservas/", minhas_reservas, name="minhas-reservas"),
    path("logout/", logout, name="logout"),
]
