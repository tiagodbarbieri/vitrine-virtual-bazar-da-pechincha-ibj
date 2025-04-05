from django.shortcuts import render
from .models import Item, Category

def listar_itens(request):
    busca = request.GET.get('busca', '').strip()
    categoria = request.GET.get('categoria', '').strip()
    lista_itens = Item.objects.all()
    
    if busca:
        lista_itens = lista_itens.filter(description__icontains=busca)
    
    if categoria:
        lista_itens = lista_itens.filter(category__name=categoria)
    
    # Consulta as categorias que deseja exibir (ajuste os filtros se necessário)
    categories = Category.objects.filter(status=True).order_by('name')
        
    return render(request, "index.html", {
        "lista_itens": lista_itens,
        "categories": categories
    })