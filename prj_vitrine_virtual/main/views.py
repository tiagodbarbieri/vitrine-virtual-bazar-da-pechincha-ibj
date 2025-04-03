from django.shortcuts import render, get_object_or_404
from .models import Category, Item

def index(request, slug_categoria=None):
    categoria = None
    lista_categorias = Category.objects.all()  # Todas as categorias
    lista_itens = Item.objects.filter(status=True)  # Itens disponíveis

    # Filtro por categoria
    if slug_categoria:
        categoria = get_object_or_404(Category, slug=slug_categoria)
        lista_itens = lista_itens.filter(categoria=categoria)

    # Busca por nome do item
    search_query = request.GET.get('search', '')
    if search_query:
        lista_itens = lista_itens.filter(name__icontains=search_query)

    contexto = {
        'categoria': categoria,
        'lista_categorias': lista_categorias,
        'lista_itens': lista_itens,
        'search_query': search_query,
    }
    return render(request, "index.html", contexto)