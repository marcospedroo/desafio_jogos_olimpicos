
from rest_framework import serializers

from modalidades.models import Competicao, Resultados


class ResultadosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Resultados
        fields = ['competicao', 'atleta', 'value', 'unidade']


class CompeticaoSerializer(serializers.HyperlinkedModelSerializer):
    resultados = ResultadosSerializer(many=True, read_only=True)

    class Meta:
        model = Competicao
        fields = ['nome', 'tipo', 'competicao_ativa', 'resultados']
