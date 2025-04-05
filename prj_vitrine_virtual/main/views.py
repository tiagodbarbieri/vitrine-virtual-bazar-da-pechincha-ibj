from django.shortcuts import render, get_object_or_404
from .models import Item, Image


def listar_itens(request):
    lista_itens = Item.objects.all()  # Obtém todos os itens
    return render(request, "index.html", {"lista_itens": lista_itens})


def detalhe(request, item_id):
    item = get_object_or_404(Item, id=item_id)  # Obtém os itens com o respectivo id
    images = Image.objects.filter(item_id=item)  # Obtém a lista de imagens referentes ao respectivo item
    return render(request, "detalhe.html", {"item": item, "images": images})
