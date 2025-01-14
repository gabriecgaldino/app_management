from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from Usuario.views import login_view
from Configurações.views import configuracoes_view, perfil_view, atualizar_perfil_view, colaboradores_view
from Organização.views import cria_setor
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', views.index, name='index'),
    path('configurações/', configuracoes_view, name='configurações'),
    path('perfil/', perfil_view, name='perfil'),
    path('atualizar-perfil/', atualizar_perfil_view, name='atualizar_perfil'),
    path('novo-setor/', cria_setor, name='novo-setor'),
    path('colaboradores/', colaboradores_view, name='colaboradores'),
    path('colaboradores/<str:matricula>/', colaboradores_view, name='colaboradores'),
]
