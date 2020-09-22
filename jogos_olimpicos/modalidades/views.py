from django.db.models import Case, When
from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.decorators import api_view

from modalidades.models import Competicao, Resultados
from modalidades.serializers import CompeticaoSerializer, ResultadosSerializer
from rest_framework.response import Response


@api_view(['POST'])
def inserir_resultado(request):
    try:
        Resultados.cadastrar_resultados(nome_competicao=request.data.get('competicao'),
                                        atleta=request.data.get('atleta'),
                                        value=request.data.get('value'),
                                        unidade=request.data.get('unidade'))
        serializer = ResultadosViewSet(data=request.data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({"message": f'{e}'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def finalizar_competicao(request):
    try:
        competicao = request.data.get('competicao')
        Competicao.objects.get(nome=competicao).encerrar_competicao()
        return Response({"competicao": competicao, "ativa": False}, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({"message": f'{e}'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def iniciar_competicao(request):
    try:
        nome = request.data.get('nome')
        tipo = request.data.get('tipo')

        if not nome or not tipo:
            raise Exception('Campos obrigatórios não preenchidos')

        Competicao.iniciar_competicao(nome=nome, tipo=tipo)
        serializer = CompeticaoViewSet(data=request.data)

        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({"message": f'{e}'}, status=status.HTTP_400_BAD_REQUEST)


class CompeticaoViewSet(viewsets.ModelViewSet):
    queryset = Competicao.objects.all().order_by('-competicao_ativa')
    serializer_class = CompeticaoSerializer
    http_method_names = ['get', 'head']

