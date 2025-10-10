from django.db.models import Sum
from main.models import Item
from users.models import ReservedItems
from datetime import date


def only_digits(cpf: str) -> str:
    numbers = ""
    for character in cpf:
        if character.isdigit():
            numbers = numbers + character
    return numbers


# Função que calcula a quantidade de itens disponíveis com base no estoque e nos itens reservados
def quantity_items_available(item: Item) -> int:
    # Quantidade de itens reservados
    reserved_items = ReservedItems.objects.filter(item_id=item).aggregate(Sum("items_quantity"))["items_quantity__sum"]

    # Quantidade de itens disponíveis = (itens do estoque - total de itens reservados)
    total_items = item.stock - (reserved_items if reserved_items is not None else 0)

    return int(total_items)


# Função que retorna o próximo segundo sábado referente ao dia atual
def next_second_saturday(date_now: date) -> date:
    if date_now < second_saturday(date_now):
        return second_saturday(date_now)
    elif date_now >= second_saturday(date_now):
        if date_now.month < 12:
            return second_saturday(date(date_now.year, date_now.month + 1, date_now.day))
        else:
            return second_saturday(date(date_now.year + 1, 1, date_now.day))


# Função que retorna a data do segundo sábado referente ao mesmo mês
def second_saturday(date_given: date) -> date:
    month = date_given.month
    year = date_given.year

    start_week_day = date(year, month, 1).weekday() + 2 if date(year, month, 1).weekday() <= 5 else 1
    second_saturday = 15 - start_week_day

    return date(year, month, second_saturday)
