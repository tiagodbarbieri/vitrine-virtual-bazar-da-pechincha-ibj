"""
URL configuration for vitrine_virtual project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path("", include("main.urls")),
    path("quem-somos/", TemplateView.as_view(template_name="quem_somos.html"), name="quem-somos"),
    path("contato/", TemplateView.as_view(template_name="contato.html"), name="contato"),
    path("admin/", admin.site.urls),
]
#altera os nomes dos sites admin
admin.site.site_title = "Vitrine virtual - admin"
admin.site.site_header = "Administração Vitrine Virtual - Bazar da pechincha"
admin.site.index_title = "Admininstração do Site"