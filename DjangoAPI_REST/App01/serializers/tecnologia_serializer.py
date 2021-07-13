from rest_framework import serializers
from ..models import Tecnologia

#Classe tecnologia Serializer que herda de um model Serializer
class TecnologiaSerializer(serializers.ModelSerializer):
    class Meta:

        #Utiliza como base para validação o model "Tecnologia".
        model = Tecnologia

        #Campos exibidos quando uma tecnologia for retornada
        fields = ('nome', )