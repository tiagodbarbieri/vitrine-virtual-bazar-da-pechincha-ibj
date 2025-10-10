from django.test import TestCase
from users.utils import only_digits


class TestarFuncaoOnlyDigits(TestCase):
    def testar_se_funcao_only_digits_retorna_somente_digitos(self):
        valor = only_digits("123.456.789-10")
        self.assertEqual(valor, "12345678910")
