from django.contrib import admin
from .models import Category, Item, Image

# Dados para login:
#   user: admin
#   password: admin123


# cria uma ação, As ações de administração do Django permitem que você
# execute uma "ação" em um objeto ou grupo de objetos. Uma ação pode ser
# usada para modificar os atributos de um objeto, excluir o objeto,
# copiá-lo e assim por diante. As ações são utilizadas principalmente para
# "ações" frequentemente executadas ou alterações em massa.
# neste caso será para ativer ou desativar o item através do atributo "status"
@admin.action(description="Ativar itens selecionados")
def ativarItem(modeLadmin, request, queryset):
    queryset.update(status=True)


@admin.action(description="Desativar itens selecionados")
def desativarItem(modeLadmin, request, queryset):
    queryset.update(status=False)


class ImageInLine(admin.TabularInline):
    model = Image
    extra = 0
    can_delete = True
    show_change_link = False


# cria uma classe "ItemAdmin" que controla como a lista aparece na Interface admin
# é necessário uma classe para cada modelo
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    fields = ["name", "description", "price", "category", "stock"]
    ordering = ["id"]
    list_display = ["id", "name", "description", "price", "stock", "status"]
    list_filter = ["name", "price", "stock", "status"]
    search_fields = ["id", "name", "description", "price", "stock", "status"]
    list_display_links = ["name"]
    actions = [ativarItem, desativarItem]
    inlines = [
        ImageInLine,
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ("name", "status")
    ordering = ["id"]
    list_display = ["id", "name", "status"]
    list_filter = ["name"]
    search_fields = ["id", "name", "status"]
    list_display_links = ["name"]
    actions = [ativarItem, desativarItem]
