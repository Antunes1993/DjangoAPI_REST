from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView
from ..services import vaga_service
from ..serializers import vaga_serializer
from rest_framework.response import Response
from ..entidades import vaga
from ..pagination import PaginacaoCustomizada

#Classe contentdo métodos que não dependem de um parâmetro de entrada ID
class VagaList(APIView):
    def get(self, request, format=None):
        paginacao = PaginacaoCustomizada()
        vagas = vaga_service.listar_vagas()

        #paginacao das vagas
        resultado = paginacao.paginate_queryset(vagas, request)

        #vagas passadas de forma paginada para o serializer
        serializer = vaga_serializer.VagaSerializer(resultado, many=True)

        #retorno das vagas paginadas
        return paginacao.get_paginated_response(serializer.data)
        #return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = vaga_serializer.VagaSerializer(data=request.data)
        if serializer.is_valid():
            titulo = serializer.validated_data["titulo"]
            descricao = serializer.validated_data["descricao"]
            salario = serializer.validated_data["salario"]
            tipo_contratacao = serializer.validated_data["tipo_contratacao"]
            local = serializer.validated_data["local"]
            quantidade = serializer.validated_data["quantidade"]
            contato = serializer.validated_data["contato"]
            tecnologias = serializer.validated_data["tecnologias"]

            #Supondo que a requisição esteja correta, iremos criar uma entidade vaga para que essa vaga seja enviada para
            #o método cadastrar vagas localizado no arquivo vaga_service.py.
            vaga_nova = vaga.Vaga(titulo=titulo, descricao=descricao, salario=salario, tipo_contratacao=tipo_contratacao,
                                  local=local, quantidade=quantidade, contato=contato, tecnologias=tecnologias)
            vaga_service.cadastrar_vagas(vaga_nova)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Classe contentdo métodos que dependem de um parâmetro de entrada ID
class VagaDetalhes(APIView):
    def get(self, request, id, format=None):
        vaga = vaga_service.listar_vagas_id(id)
        serializer = vaga_serializer.VagaSerializer(vaga)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id, format=None):
        vaga_antiga = vaga_service.listar_vagas_id(id)
        serializer = vaga_serializer.VagaSerializer(vaga_antiga, data=request.data)
        if serializer.is_valid():
            titulo = serializer.validated_data["titulo"]
            descricao = serializer.validated_data["descricao"]
            salario = serializer.validated_data["salario"]
            tipo_contratacao = serializer.validated_data["tipo_contratacao"]
            local = serializer.validated_data["local"]
            quantidade = serializer.validated_data["quantidade"]
            contato = serializer.validated_data["contato"]
            tecnologias = serializer.validated_data["tecnologias"]

            vaga_nova = vaga.Vaga(titulo=titulo, descricao=descricao, salario=salario,
                                  tipo_contratacao=tipo_contratacao,
                                  local=local, quantidade=quantidade, contato=contato, tecnologias=tecnologias)

            #Enviar vaga antiga e vaga nova para o método editar_vaga no arquivo vaga_service.
            vaga_service.editar_vagas(vaga_antiga, vaga_nova)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        vaga = vaga_service.listar_vagas_id(id)
        vaga_service.remover_vaga(vaga)
        return Response(status=status.HTTP_204_NO_CONTENT)