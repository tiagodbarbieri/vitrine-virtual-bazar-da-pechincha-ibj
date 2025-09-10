from django.db import models
from django.contrib.auth.models import User


GENDER = [("M", "Masculino"), ("F", "Feminino"), ("O", "Outro")]


# Estendendo o modelo do Usuário existente
class UserInfo(models.Model):
    cpf = models.CharField(max_length=14)
    birthday = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER, default="M")
    phone_number = models.CharField(max_length=20)
    privacy_police = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
