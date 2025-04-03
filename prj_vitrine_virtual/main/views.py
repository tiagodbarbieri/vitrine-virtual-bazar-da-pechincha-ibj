from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Category, Item


def listar_itens (request, slug_categoria=None):
    categoria = None
    lista_categorias = Category.objects.all()
    lista_itens = Item.objects.filter(disponivel=True)
    if slug_categoria:
        categoria = get_object_or_404(Category, slug=slug_categoria)
        lista_itens = Item.objects.filter(categoria=categoria) 
    contexto = {'categoria': categoria,'lista_categorias': lista_categorias,'lista_itens': lista_itens}
    return render(request, "item/listar.html",contexto)
def detalhes_item(request, id, slug):
    item = get_object_or_404(Item, id=id, slug=slug_item, disponivel=True)
    contexto = {'item': item}
    return render(request, "item/detalhes.html", contexto) 