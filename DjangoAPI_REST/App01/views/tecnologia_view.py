from rest_framework.views import APIView
from ..services import tecnologia_service
from ..serializers import tecnologia_serializer
from rest_framework.response import Response
from rest_framework import status
from ..entidades import tecnologia

#Classe contendo métodos que não dependem de um parâmetro de entrada ID
class TecnologiaList(APIView):
    def get(self, request, format=None):

        #Chama o método de listar as tecnologias a partir do tecnologia_service
        tecnologias = tecnologia_service.listar_tecnologias()

        #Validação dos dados pelo serializer
        serializer = tecnologia_serializer.TecnologiaSerializer(tecnologias, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):

        # Enviaremos as informações para o serializer utilizando um método que está no service.
        # O serializer irá validar as informações inseridas e, caso estejam válidas, irá persisti-las no banco de dados.
        serializer = tecnologia_serializer.TecnologiaSerializer(data=request.data)
        if serializer.is_valid():
            nome = serializer.validated_data["nome"]
            tecnologia_nova = tecnologia.Tecnologia(nome=nome)
            tecnologia_bd = tecnologia_service.cadastrar_tecnologia(tecnologia_nova)
            return Response(serializer.data, status.HTTP_201_CREATED)

        #Caso haja um problema na requisição, o serializer não será válido e então devemos retornar um cód. informando o erro.
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Classe contentdo métodos que dependem de um parâmetro de entrada ID
class TecnologiaDetalhes(APIView):
    def get(self, request, id, format=None):
        tecnologia = tecnologia_service.listar_tecnologia_id(id)
        serializer = tecnologia_serializer.TecnologiaSerializer(tecnologia)
        #Se o id não existir a própria função "listar_tecnologia_id" já irá retornar um código 404.
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id, format=None):
        tecnologia_antiga = tecnologia_service.listar_tecnologia_id(id)
        serializer = tecnologia_serializer.TecnologiaSerializer(tecnologia_antiga, data=request.data)
        if serializer.is_valid():
            nome = serializer.validated_data["nome"]
            tecnologia_nova = tecnologia.Tecnologia(nome=nome)
            tecnologia_service.editar_tecnologia(tecnologia_antiga, tecnologia_nova)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        tecnologia = tecnologia_service.listar_tecnologia_id(id)
        tecnologia_service.remover_tecnologia(tecnologia)
        return Response(status=status.HTTP_204_NO_CONTENT)