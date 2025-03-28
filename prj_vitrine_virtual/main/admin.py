from django.contrib import admin
from .models import Category, Item, Image

# Dados para login:
#   user: admin_ibj
#   password: ibj_2025

# Register your models here.

admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Image)
