from django.contrib import admin

# Register your models here.
# importa os modelos de models.py
from .models import Category
from .models import Item
from .models import Image

# add cada modelo(tabela na interface admin
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Image)