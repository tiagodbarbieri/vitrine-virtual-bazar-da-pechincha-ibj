from django.urls import path

from . import views
from main.views import detalhe
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.listar_itens, name="index"),
    path("detalhe/<int:item_id>", detalhe, name="detalhe"),
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)  # Mapeamento para carregar as imagens da pasta upload
