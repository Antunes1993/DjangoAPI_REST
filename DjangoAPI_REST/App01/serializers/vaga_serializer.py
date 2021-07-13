from rest_framework import serializers
from ..models import Vaga

#Valida a requisição e determina como os dados serão exibidos para o usuário.
class VagaSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()
    class Meta:
        model = Vaga
        fields = ('titulo', 'descricao', 'salario', 'local', 'quantidade', 'contato', 'tipo_contratacao', 'tecnologias')

