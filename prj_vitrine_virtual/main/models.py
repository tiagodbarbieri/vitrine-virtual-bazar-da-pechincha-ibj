# Após qualquer alteração na estrutura deste arquivo, rodar os comandos:
# python manage.py makemigrations "nome_do_app" --> para criar migrações para suas modificações
# python manage.py migrate                      --> para aplicar suas modificações no banco de dados

from django.db import models


# Tabela de categorias
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    # slug = models.SlugField(max_length=150, unique=True, db_index=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} - {self.name}"


# Tabela de itens
class Item(models.Model):
    id = models.BigAutoField(primary_key=True)
    # slug = models.SlugField(max_length=150, unique=True, db_index=True)
    name = models.CharField(max_length=100, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name="items")

    def __str__(self):
        return f"{self.id} - {self.name}\n{self.description}\nR${self.price},{self.creation_date},{self.category.name}"


# Tabela de imagens
class Image(models.Model):
    id = models.BigAutoField(primary_key=True)
    file = models.ImageField(upload_to="upload/", blank=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="images")

    def __str__(self):
        return f"{self.file.name} ({self.file.size}) bytes"
