from django import forms
from .models import Category


class Search(forms.Form):
    order_list = [("1", "mais recentes"), ("2", "menor valor"), ("3", "maior valor"), ("4", "nome")]
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label="Categoria:", empty_label="todas")
    word = forms.CharField(required=False, label="Palavra chave:")
    order = forms.ChoiceField(choices=order_list, label="Ordenar por:")

    class Meta:
        model = Category
        fields = ("category",)
