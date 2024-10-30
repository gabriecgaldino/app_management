"""
URL configuration for Sistema_de_Gestão_Empresarial project.

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
from django.contrib.auth.views import LogoutView
from django.urls import path
from Usuario.views import registro, login_view, change_data_user
from Sistema_de_Gestão_Empresarial.views import home
from Produto.views import excluir_produto, editar_produto
from Estoque.views import estoque_view
from Vendas.views import vendas
from Contatos.views import buscar_contatos


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),
    path('register/', registro, name='registro'),
    path('home/', home, name='home'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('update-user/', change_data_user, name='update-user'),
    path('estoque/', estoque_view, name='estoque'),
    path('estoque/excluir/<int:produto_id>/',
         excluir_produto, name='excluir_produto'),
    path('produto/editar/<int:produto_id>/', editar_produto, name='editar_produto'),
    path('vendas/', vendas, name='vendas'),
    path('buscar-contatos/', buscar_contatos, name='buscar_contatos')
]
