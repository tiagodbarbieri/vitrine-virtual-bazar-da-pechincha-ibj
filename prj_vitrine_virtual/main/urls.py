from django.urls import path
from main.views import home
from main.views import detalhe


urlpatterns = [
    path("", home, name="home-page"),
    path("detalhe/<str:slug>", detalhe, name="detalhe"),
]
