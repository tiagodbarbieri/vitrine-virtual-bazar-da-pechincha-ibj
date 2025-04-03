from django.shortcuts import render
from .models import Item

def listar_itens(request):
    lista_itens = Item.objects.all()  # Obtém todos os itens
    return render(request, "index.html", {"lista_itens": lista_itens})
def detalhe(request):
    return render(request, 'detalhe.html')