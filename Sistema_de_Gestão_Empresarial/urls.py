from django.contrib import admin
from django.urls import path
from Usuario.views import login_view
from .views import index
from Configurações.views import configuracoes_view, perfil_view, atualizar_perfil_view, colaboradores_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('', index, name='index'),
    path('configurações/', configuracoes_view, name='configurações'),
    path('perfil/', perfil_view, name='perfil'),
    path('atualizar-perfil/', atualizar_perfil_view, name='atualizar_perfil'),
    path('colaboradores/', colaboradores_view, name='colaboradores'),
]
