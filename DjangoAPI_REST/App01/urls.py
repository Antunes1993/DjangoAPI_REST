from django.urls import path, include
from .views import tecnologia_view
from .views import vaga_view
from .views import usuario_view

urlpatterns = [
    path('tecnologias/', tecnologia_view.TecnologiaList.as_view(), name='tecnologia-list'),
    path('tecnologias/<int:id>', tecnologia_view.TecnologiaDetalhes.as_view(), name='tecnologia-list-detalhes'),
    path('vagas/', vaga_view.VagaList.as_view(), name='vaga-list'),
    path('vagas/<int:id>', vaga_view.VagaDetalhes.as_view(), name='vaga-list-detalhes'),
    path('usuarios/', usuario_view.UsuarioList.as_view(), name='usuario-list'),

]
