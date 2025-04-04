from django.shortcuts import render
from .forms import Search


def home(request):
    if request.method == "GET":
        # Buscar todos os itens e listá-los por mais recentes...
        # Mostrar por página no máximo 16 items

        return render(request, "home.html", {"form": Search})

    elif request.method == "POST":
        # Capturando os dados enviados
        form = Search(request.POST)

        # Verificando se os dados são válidos
        if form.is_valid():
            category = form.cleaned_data["category"]
            word = form.cleaned_data["word"]
            order = form.cleaned_data["order"]

            # Buscar os itens no banco de dados conforme categoria e palavra chave
            # Ordenar os itens

            print(category)
            print(word)
            print(order)

        return render(request, "home.html", {"form": form})
