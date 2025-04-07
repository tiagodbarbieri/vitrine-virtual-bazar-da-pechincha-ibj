from django import forms
from .models import Category


def categories():
    cat_list = [("0", "todas")]
    for obj in Category.objects.all():
        cat_list.append((obj.id, obj.name))
    return cat_list


class Search(forms.Form):
    order_list = [("1", "mais recentes"), ("2", "menor valor"), ("3", "maior valor"), ("4", "nome")]
    category = forms.ChoiceField(choices=categories(), label="Categoria:")
    word = forms.CharField(required=False, label="Palavra chave:")
    order = forms.ChoiceField(choices=order_list, label="Ordenar por:")
