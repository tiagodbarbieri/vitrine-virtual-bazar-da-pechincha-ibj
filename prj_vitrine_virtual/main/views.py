from django.shortcuts import render
from .models import Item


def listar_itens(request):
    itens = Item.objects.all()  # Busca todos os objetos da classe Item
    return render(request, "index.html", {"itens": itens})  # Passa os itens para o template
