from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from Usuario.views import login_view, busca_colaborador_api, atualiza_dados_colaborador
from Configurações.views import configuracoes_view, perfil_view, atualizar_perfil_view, colaboradores_view
from Organização.views import cria_setor, listar_cargos_api, listar_setores_api
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', views.index, name='index'),
    path('configurações/', configuracoes_view, name='configurações'),
    path('perfil/', perfil_view, name='perfil'),
    path('atualizar-perfil/', atualizar_perfil_view, name='atualizar_perfil'),
    path('colaboradores/', colaboradores_view, name='colaboradores'),
    path('novo-setor/', cria_setor, name='novo-setor'),
    path('api/cargos/', listar_cargos_api, name='listar_cargos'),
    path('api/setores/', listar_setores_api, name='listar_setores'),
    path('api/colaboradores/', busca_colaborador_api, name='busca_colaborador'),
    path('api/colaboradores/atualizar-dados/', atualiza_dados_colaborador, name='atualiza_colaborador')
]
