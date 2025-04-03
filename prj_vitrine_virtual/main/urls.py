from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path("", views.index, name="index"),
    path("categoria/<slug:slug_categoria>/", views.index, name="filtrar_por_categoria"),
]
