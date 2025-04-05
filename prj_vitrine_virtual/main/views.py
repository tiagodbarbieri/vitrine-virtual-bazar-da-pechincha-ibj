from django.shortcuts import render
from .models import Item

def listar_itens(request):
    busca = request.GET.get('busca', '')
    if busca:
        lista_itens = Item.objects.filter(description__icontains=busca)
    else:
        lista_itens = Item.objects.all()
    return render(request, "index.html", {"lista_itens": lista_itens})