from django.db import models

class Produto(models.Model):

 nome = models.CharField(max_length= 50)
 marca_produto = models.CharField(max_length=200)
 descricao = models.CharField(max_length=200)
 quantidade = models.IntegerField()
 preco = models.FloatField()


def __str__(self):
    return self.nome
