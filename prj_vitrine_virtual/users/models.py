from django.db import models
from django.contrib.auth.models import User
from main.models import Item


GENDER = [("M", "Masculino"), ("F", "Feminino"), ("O", "Outro")]


# Estendendo o modelo do Usuário existente
class UserInfo(models.Model):
    cpf = models.CharField(max_length=14)
    birthday = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER, default="M")
    phone_number = models.CharField(max_length=20)
    privacy_police = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


# Tabela dos itens reservados
class ReservedItems(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    items_quantity = models.PositiveBigIntegerField()
    reservation_date = models.DateField()
    pickup_date = models.DateField()

    class Meta:
        unique_together = ("user_id", "item_id")  # garante que a combinação seja única
