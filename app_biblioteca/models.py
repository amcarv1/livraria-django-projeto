from django.db import models

DISPONIVEL = (
    ('Sim', 'Sim'),
    ('Não', 'Não')
)

class Livro(models.Model):
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=100) 
    editora = models.CharField(max_length=100) 
    edicao = models.CharField('Edição', max_length=100)
    ano_publicacao = models.DateField('Ano da Publicação (dd/mm/aaaa)',auto_now_add=False) 
    estoque = models.IntegerField()
    disponivel = models.CharField('Disponível', max_length=3, choices=DISPONIVEL)

    def __str__(self):
        return self.nome