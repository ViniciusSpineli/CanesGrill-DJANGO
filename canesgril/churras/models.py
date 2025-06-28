from django.db import models
from datetime import datetime

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    email = models.EmailField('Email', max_length=100)
    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preco', decimal_places=2, max_digits=8)
    estoque = models.IntegerField('Quantidade em estoque')
    def __str__(self):
        return self.nome
    

class Prato(models.Model):
    nome_prato = models.CharField(max_length=100)
    ingredientes = models.TextField()
    modo_preparo = models.CharField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=10)
    categoria = models.CharField(max_length=100)
    date_prato = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.nome_prato

