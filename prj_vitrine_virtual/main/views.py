from django.shortcuts import render
from django.db.models import Q
from .forms import Search
from .models import Item


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
        images_paths = []
        for item in items:
            image_path = item.first_image().file.name if item.first_image() else ""
            images_paths.append(image_path)

        return render(
            request, "home.html", {"form": form, "items": items, "items_and_images": zip(items, images_paths)}
        )
