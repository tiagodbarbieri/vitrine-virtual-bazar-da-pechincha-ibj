from django.db import models
from django.contrib.auth.models import User


# Estendendo o modelo Usuário existente
class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
