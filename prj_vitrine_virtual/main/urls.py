from django.urls import path

from . import views
from main.views import detalhe

urlpatterns = [
    path("", views.listar_itens, name="index"),
    path('detalhe/', detalhe, name='detalhe'),
]