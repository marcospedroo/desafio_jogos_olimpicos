from django.core.exceptions import ObjectDoesNotExist
from django.db import models


# Create your models here.
class Competicao(models.Model):
    nome = models.CharField(max_length=200, primary_key=True)
    tipo = models.CharField(max_length=1, choices=[('L', 'Lançamento de Dardo'), ('C', '100m rasos')])
    competicao_ativa = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        if not self.pk:
            try:
                Competicao.objects.get(nome=self.nome)
                raise Exception('Já existe uma competição com este nome')
            except ObjectDoesNotExist:
                super(Competicao, self).save(*args, **kwargs)

        super(Competicao, self).save(*args, **kwargs)

    @staticmethod
    def get_competicao_ativa(nome):
        try:
            competicao = Competicao.objects.get(nome=nome, competicao_ativa=True)
        except ObjectDoesNotExist:
            competicao = []
        return competicao

    @staticmethod
    def iniciar_competicao(nome, tipo):
        competicao = Competicao.objects.create(nome=nome, tipo=tipo, competicao_ativa=True)
        competicao.save()

        return competicao

    def encerrar_competicao(self):
        self.competicao_ativa = False
        self.save()


class Resultados(models.Model):
    competicao = models.ForeignKey(Competicao, on_delete=models.PROTECT, related_name='resultados')
    atleta = models.CharField(max_length=200)
    value = models.FloatField()
    unidade = models.CharField(max_length=1)

    class Meta:
        ordering = ['-value']

    def save(self, *args, **kwargs):
        if not self.pk:
            if self.competicao.tipo == 'C':
                if Resultados.objects.filter(competicao=self.competicao, atleta=self.atleta):
                    raise Exception('O valor informado já foi cadastrado para este atleta nesta competição')
            elif self.competicao.tipo == 'L':
                if Resultados.objects.filter(competicao=self.competicao, atleta=self.atleta).count() >= 3:
                    raise Exception('Este atleta já possui 3 resultados cadastrados para esta competição')
        super(Resultados, self).save(*args, **kwargs)

    @staticmethod
    def cadastrar_resultados(nome_competicao, atleta, value, unidade):
        competicao = Competicao.get_competicao_ativa(nome_competicao)
        if competicao:
            Resultados.objects.create(competicao=competicao, atleta=atleta, value=value, unidade=unidade)
        else:
            raise Exception('A competicao está inativa ou não existe')


