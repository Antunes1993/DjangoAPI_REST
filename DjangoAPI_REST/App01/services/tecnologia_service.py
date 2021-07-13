#Aqui serão determinados os métodos do nosso crud.
from ..models import Tecnologia
from django.http import Http404

def listar_tecnologias():
    tecnologias = Tecnologia.objects.all()
    return tecnologias

def cadastrar_tecnologia(tecnologia):
    return Tecnologia.objects.create(nome=tecnologia.nome)

def listar_tecnologia_id(id):

    #Tenta achar uma tecnologia no banco com um determinado id
    try:
        return Tecnologia.objects.get(id=id)

    #Caso não encontre a tecnologia retorna erro 404.
    except Tecnologia.DoesNotExist:
        raise Http404

def editar_tecnologia(tecnologia_antiga, tecnologia_nova):
    tecnologia_antiga.nome = tecnologia_nova.nome
    tecnologia_antiga.save(force_update = True)

def remover_tecnologia(tecnologia):
    tecnologia.delete()