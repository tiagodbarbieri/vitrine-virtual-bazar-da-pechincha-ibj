from django.contrib.auth.models import User
from django.test import TestCase
from datetime import datetime, date
from main.models import Category, Item
from users.models import ReservedItems
from users.utils import only_digits
from users.utils import quantity_items_available
from users.utils import second_saturday
from users.utils import next_second_saturday


class TestarFuncaoOnlyDigits(TestCase):
    def testar_se_funcao_only_digits_retorna_somente_digitos(self):
        valor = only_digits("123.456.789-10")
        self.assertEqual(valor, "12345678910")


class TestarFuncaoQuantityItemsAvailable(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            id=1,
            name="brinquedos",
            slug="brinquedos",
            creation_date=datetime.now(),
            update_date=datetime.now(),
        )
        self.item = Item.objects.create(
            id=1,
            name="Carrinho de corrida",
            slug="carrinho-de-corrida",
            description="",
            price=15,
            stock=10,
            creation_date=datetime.now(),
            update_date=datetime.now(),
            category=self.category,
        )
        self.user = User.objects.create_user(
            username="testuser",
            password="1234",
            email="teste@example.com",
        )
        self.reserved_item = ReservedItems.objects.create(
            user=self.user,
            item=self.item,
            items_quantity=3,
            reservation_date=datetime.now(),
            pickup_date=datetime.now(),
        )

    def testar_se_funcao_retorna_valor_correto(self):
        qty_available = quantity_items_available(self.item)
        self.assertEqual(qty_available, 7)


class TestarFuncaoSecondSaturday(TestCase):
    def testar_se_funcao_retorna_o_segundo_sabado_do_mes(self):
        secondSaturday = second_saturday(date(2025, 10, 15))
        self.assertEqual(secondSaturday, date(2025, 10, 11))


class TestarFuncaoNextSecondSaturday(TestCase):
    def testar_no_mesmo_mes(self):
        next = next_second_saturday(date(2025, 10, 10))
        self.assertEqual(next, date(2025, 10, 11))

    def testar_no_mes_seguinte_01(self):
        next = next_second_saturday(date(2025, 10, 11))
        self.assertEqual(next, date(2025, 11, 8))

    def testar_no_mes_seguinte_02(self):
        next = next_second_saturday(date(2025, 10, 12))
        self.assertEqual(next, date(2025, 11, 8))

    def testar_no_proximo_ano(self):
        next = next_second_saturday(date(2025, 12, 15))
        self.assertEqual(next, date(2026, 1, 10))
