from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .forms import Search
from .models import Item, Image


def get_order(order: int) -> str:
    """Return the order string"""
    match order:
        case 1:
            return "-update_date"
        case 2:
            return "price"
        case 3:
            return "-price"
        case 4:
            return "name"


def home(request):
    if request.method == "GET":
        # Capturando os dados enviados
        form = Search(request.GET)

        # Verificando se os dados são válidos
        if form.is_valid():
            category = form.cleaned_data["category"]
            word = form.cleaned_data["word"]
            order = get_order(int(form.cleaned_data["order"]))
        else:
            category = "0"
            word = ""
            order = get_order(1)

        # Buscar os itens no banco de dados conforme categoria e palavra chave
        # Ordenar os itens
        if category == "0" and word == "":
            items = Item.objects.all().order_by(order)
        elif category == "0" and word != "":
            items = Item.objects.filter(Q(name__contains=word) | Q(description__contains=word)).order_by(order)
        elif category != "0" and word == "":
            items = Item.objects.filter(category_id=category).order_by(order)
        elif category != "0" and word != "":
            items = Item.objects.filter(
                Q(category_id=category) & (Q(name__contains=word) | Q(description__contains=word))
            ).order_by(order)

        # Criar lista com as respectivas imagens de cada item (apenas uma imagem)
        images_urls = []
        for item in items:
            image_url = item.first_image().file.url if item.first_image() else ""
            images_urls.append(image_url)

        return render(request, "home.html", {"form": form, "items": items, "items_and_images": zip(items, images_urls)})


def listar_itens(request):
    lista_itens = Item.objects.all()  # Obtém todos os itens
    return render(request, "index.html", {"lista_itens": lista_itens})


def detalhe(request, item_id):
    item = get_object_or_404(Item, id=item_id)  # Obtém os itens com o respectivo id
    images = Image.objects.filter(item_id=item)  # Obtém a lista de imagens referentes ao respectivo item
    return render(request, "detalhe.html", {"item": item, "images": images})
