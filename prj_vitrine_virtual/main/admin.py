from django.contrib import admin
from .models import Category, Item, Image

# Dados para login:
#   user: admin
#   password: admin123

# Register your models here.
# Adiciona cada modelo/tabela na interface admin
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Image)
