from django.contrib import admin
from django.urls import path
from Usuario.views import login_view
from .views import index
from Configurações.views import configuracoes_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('', index, name='index'),
    path('configurações/', configuracoes_view, name='configurações')
    
]
