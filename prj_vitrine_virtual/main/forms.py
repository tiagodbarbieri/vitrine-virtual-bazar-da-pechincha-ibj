from django import forms
from .models import Category


def categories():
    cat_list = [("0", "todas")]
    for obj in Category.objects.all():
        cat_list.append((obj.id, obj.name))
    return cat_list


class Search(forms.Form):
    order_list = [("1", "por nome"), ("2", "mais recentes"), ("3", "menor valor"), ("4", "maior valor")]
    category = forms.ChoiceField(choices=categories(), label="Categoria")
    word = forms.CharField(required=False, label="Palavra chave:", initial="Digite...")
    order = forms.ChoiceField(choices=order_list, label="Ordenar por:")
