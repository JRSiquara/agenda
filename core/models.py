from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Evento(models.Model):     # Esta classe cria a tabela evento.
    titulo = models.CharField(max_length=100)  # "models." já importado na 1a linha from django.
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True)  # Ao inserir o registro preenche automaticamente.
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:                 # Após executar o comando para criar as tabelas no terminal, o django por
        db_table = 'evento'     # default coloca o nome do app (neste caso é "core" no nome da tabela "core_evento".
                                # Para definir qual o nome da tabela tem que incluir esta classe Meta: determinando
                                # o real nome da tabela.

    def __str__(self):
        return self.titulo  # Faz aparecer na tela o nome do evento.
