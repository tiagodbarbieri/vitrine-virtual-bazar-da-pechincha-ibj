from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import JsonResponse
from main.forms import Search
from main.models import Item, Image
from users.utils import quantity_items_available

ITEMS_PER_PAGE = 4  # ✅ Itens fixos por página

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
        form = Search(request.GET)

        if form.is_valid():
            category = form.cleaned_data["category"]
            word = form.cleaned_data["word"]
            order = get_order(int(form.cleaned_data["order"]))
        else:
            category = "0"
            word = form.cleaned_data.get("word", "")
            try:
                order = get_order(int(form.cleaned_data["order"]))
            except KeyError:
                order = get_order(1)

        if category == "0" and word == "":
            items = Item.objects.all().order_by(order)
        elif category == "0" and word != "":
            items = Item.objects.filter(Q(name__contains=word) | Q(description__contains=word)).order_by(order)
        elif category != "0" and word == "":
            items = Item.objects.filter(category_id=category).order_by(order)
        else:
            items = Item.objects.filter(
                Q(category_id=category) & (Q(name__contains=word) | Q(description__contains=word))
            ).order_by(order)

        # ✅ Paginação fixa no servidor
        page_number = request.GET.get("page", 1)
        paginator = Paginator(items, ITEMS_PER_PAGE)
        page_obj = paginator.get_page(page_number)

        # ✅ Resposta AJAX
        if request.headers.get("x-requested-with", "").lower() == "xmlhttprequest":
            items_data = []
            for item in page_obj:
                items_data.append({
                    "name": item.name,
                    "price": item.price,
                    "slug": item.slug,
                    "image_url": item.first_image().file.url if item.first_image() else "/static/img/imagem_nao_diponivel.jpg"
                })
            return JsonResponse({"items": items_data, "has_next": page_obj.has_next()})

        return render(request, "home.html", {
            "form": form,
            "page_obj": page_obj,
        })


def detalhe(request, slug):
    item = get_object_or_404(Item, slug=slug)
    images = Image.objects.filter(item_id=item)
    total_items = quantity_items_available(item)

    return render(request, "detalhe.html", {"item": item, "images": images, "total_items": total_items})
