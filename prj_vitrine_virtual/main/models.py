# Após qualquer alteração na estrutura deste arquivo, rodar os comandos:
# python manage.py makemigrations "nome_do_app" --> para criar migrações para suas modificações
# python manage.py migrate                      --> para aplicar suas modificações no banco de dados

from django.db import models
from django.utils.text import slugify
from pathlib import Path


# Tabela de categorias
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)
    status = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
        ordering = ["name"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"


# Tabela de itens
class Item(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=150, db_index=True, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    status = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name="items")

    class Meta:
        verbose_name = "item"
        verbose_name_plural = "itens"
        ordering = ["name"]

    def first_image(self):
        return Image.objects.filter(item_id=self).order_by("id").first()

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1

            while Item.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.id} - {self.name}"


# Tabela de imagens
class Image(models.Model):
    id = models.BigAutoField(primary_key=True)
    file = models.ImageField(upload_to="items/")
    status = models.BooleanField(default=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="images")

    class Meta:
        verbose_name = "imagem"
        verbose_name_plural = "imagens"
        ordering = ["id"]

    def __str__(self):
        return f"{self.id} - {Path(self.file.name).name}"
