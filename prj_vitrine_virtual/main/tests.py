from django.test import TestCase
from django.urls import reverse
from datetime import datetime
from main.models import Category, Item


class TestarPaginasGerais(TestCase):
    def testar_se_home_carrega_completamente(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "BAZAR MISSIONÁRIO IBJ")

    def testar_se_home_page_carrega_completamente(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "BAZAR MISSIONÁRIO IBJ")

    def testar_se_quem_somos_carrega_completamente(self):
        response = self.client.get(reverse("quem-somos"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "quem_somos.html")
        self.assertContains(response, "QUEM SOMOS")

    def testar_se_contado_carrega_completamente(self):
        response = self.client.get(reverse("contato"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "contato.html")
        self.assertContains(response, "CONTATE-NOS")


class TestarPaginaDetalhe(TestCase):
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
            stock=2,
            creation_date=datetime.now(),
            update_date=datetime.now(),
            category=self.category,
        )

    def testar_se_detalhe_carrega_completamente(self):
        response = self.client.get(reverse("detalhe", kwargs={"slug": "carrinho-de-corrida"}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "detalhe.html")
        self.assertContains(response, "Carrinho de corrida")
