# Após qualquer alteração na estrutura deste arquivo, rodar os comandos:
# python manage.py makemigrations "nome_do_app" --> para criar migrações para suas modificações
# python manage.py migrate                      --> para aplicar suas modificações no banco de dados

from django.db import models
from django.utils.text import slugify


# Tabela de categorias
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)
    status = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
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
        return f"{self.id} - {self.name}\n{self.description}\nR${self.price},{self.creation_date},{self.category.name}"


# Tabela de imagens
class Image(models.Model):
    id = models.BigAutoField(primary_key=True)
    file = models.ImageField(upload_to="items/", blank=True)
    status = models.BooleanField(default=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="images")

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"{self.file.name} ({self.file.size}) bytes"
