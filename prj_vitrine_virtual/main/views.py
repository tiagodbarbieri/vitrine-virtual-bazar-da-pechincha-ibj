from django.shortcuts import render
from .models import Item, Category

def index(request):
    category_id = request.GET.get('category')  # Obtém o ID da categoria selecionada
    categories = Category.objects.all()  # Obtém todas as categorias

    if category_id:
        itens = Item.objects.filter(category_id=category_id)  # Filtra os itens pela categoria
    else:
        itens = Item.objects.all()  # Exibe todos os itens se nenhuma categoria for selecionada

    return render(request, 'index.html', {
        'itens': itens,
        'categories': categories,
    })