from django.db.models import Sum
from main.models import Item
from users.models import ReservedItems


def only_digits(cpf: str) -> str:
    numbers = ""
    for character in cpf:
        if character.isdigit():
            numbers = numbers + character
    return numbers


if __name__ == "__main__":
    print(only_digits("498.518.215-00"))


# Função que calcula a quantidade de itens disponíveis com base no estoque e nos itens reservados
def quantity_items_available(item: Item) -> int:
    # Quantidade de itens reservados
    reserved_items = ReservedItems.objects.filter(item_id=item).aggregate(Sum("items_quantity"))["items_quantity__sum"]

    # Quantidade de itens disponíveis = (itens do estoque - total de itens reservados)
    total_items = item.stock - (reserved_items if reserved_items is not None else 0)

    return int(total_items)
