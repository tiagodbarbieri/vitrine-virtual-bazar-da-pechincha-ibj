from django.urls import path
from . import views
from main.views import detalhe


urlpatterns = [
    path("", views.home, name="home-page"),
    path("detalhe/<str:slug>", detalhe, name="detalhe"),
]
