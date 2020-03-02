from django.urls import path
from .views import entrar, sair, cadastrar

urlpatterns = [
    path('entrar/', entrar, name='entrar'),
    path('sair/', sair, name='sair'),
    path('cadastrar/', cadastrar, name='cadastrar'),

]