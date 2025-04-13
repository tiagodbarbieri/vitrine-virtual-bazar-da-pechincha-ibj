from django.contrib import admin
# importa os modelos de models.py para a interface de admin
from .models import Category, Item, Image

# Dados para login:
#   user: admin
#   password: admin123

#cria uma ação, As ações de administração do Django permitem que você 
# execute uma "ação" em um objeto ou grupo de objetos. Uma ação pode ser 
# usada para modificar os atributos de um objeto, excluir o objeto, 
# copiá-lo e assim por diante. As ações são utilizadas principalmente para 
# "ações" frequentemente executadas ou alterações em massa. 
# neste caso será para ativer ou desativar o item atraves do atributo "status" 
@admin.action(description="Ativar itens selecioinados")
def ativarItem(modeLadmin, request, queryset):
    queryset.update(status=True)

@admin.action(description="Desativar itens selecioinados")
def desativarItem(modeLadmin, request, queryset):
    queryset.update(status=False)


# cria uma classe "itemAdmin" que controla como a lista apareçe na Interface admin, é necessário uma classe para cada modelo
class itemAdmin(admin.ModelAdmin):
#fieldsets para controlar o layout das páginas “adicionar” e “editar” do admin.
#fieldsets é uma lista de tuplas duplas, em que cada tupla dupla representa um 
# <fieldset> sobre a página de formulário do admin. (Um <fieldset> é uma “seção” do formulário.)
#As tuplas duplas estão no formato (name, field_options), onde name é uma string
# representando o título do fieldset e field_options é um dicionário com informações sobre o fieldset, incluíndo uma lista de campos para serem mostrados nele.
    fieldsets = (
        (None, {
            "fields": ("name", "description", "price", "category"
                
            ),
        }),
    )
    
    list_display = ["name", "description", "price", "stock", "status"]
    readonly_fields = ["stock"]
    list_filter = ["name"]
    search_fields = ["name", "description", "price", "stock", "status"]
    actions = [ativarItem, desativarItem]
    
    
   
class categoryAdmin(admin.ModelAdmin):
    fieldsets = ((None, {"fields": ("name","status"),}),)    
    list_display = ["id", "name", "status"]
    list_filter = ["name"]
    search_fields = ["id", "name", "status"] 
    actions = [ativarItem, desativarItem]
    


class imageAdmin(admin.ModelAdmin):
    list_display = ["id", "file", "status", "item_id"]
    sortable_by = ["id"]
    search_fields = ["file", "item_id"]



# add cada modelo/tabela na interface admin, add também as class admin, se não estiver aqui, não aprece no site
admin.site.register(Category, categoryAdmin)
admin.site.register(Item, itemAdmin)
admin.site.register(Image, imageAdmin)
