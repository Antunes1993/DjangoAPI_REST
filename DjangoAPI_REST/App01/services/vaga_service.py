#Aqui serão determinados os métodos do nosso crud.
from django.http import Http404

from .tecnologia_service import listar_tecnologia_id
from ..models import Vaga

def listar_vagas():
    vagas = Vaga.objects.all()
    return vagas

def cadastrar_vagas(vaga):
    #Aqui não entrará o atributo tecnologias, pois iremos relacionar varias tecnologias á vaga.
    vaga_bd = Vaga.objects.create(titulo=vaga.titulo, descricao=vaga.descricao, salario=vaga.salario,
                                  tipo_contratacao=vaga.tipo_contratacao, local=vaga.local, quantidade=vaga.quantidade,
                                  contato=vaga.contato)

    vaga_bd.save()
    for i in vaga.tecnologias:
        #Usamos o método de retonar tecnologia por id para relacionar uma determinada tecnologia a nossa vaga.
        tecnologia = listar_tecnologia_id(i.id)
        vaga_bd.tecnologias.add(tecnologia)

def listar_vagas_id(id):
    try:
        return Vaga.objects.get(id=id)
    except Vaga.DoesNotExist:
        raise Http404

def editar_vagas(vaga_antiga, vaga_nova):
    vaga_antiga.titulo = vaga_nova.titulo
    vaga_antiga.descricao = vaga_nova.descricao
    vaga_antiga.salario = vaga_nova.salario
    vaga_antiga.tipo_contratacao = vaga_nova.tipo_contratacao
    vaga_antiga.local = vaga_nova.local
    vaga_antiga.quantidade = vaga_nova.quantidade
    vaga_antiga.contato = vaga_nova.contato
    vaga_antiga.tecnologias.set(vaga_nova.tecnologias)

    vaga_antiga.save(force_update=True)

def remover_vaga(vaga):
    vaga.delete()