from django.db import models
from datetime import datetime

class Contatos(models.Model):
    CATEGORIA_BASE = (
        ('F','Familia'),
        ('A','Amigo'),
        ('S','Serviço'),
        ('R','Represetantes')
    )

    nome = models.CharField(max_length=50, null=False, blank=False)
    sobrenome = models.CharField(max_length=50, null=False, blank=False)
    telefone = models.CharField(max_length=15, null=False,blank=False)
    email = models.EmailField(max_length=100, null=False, blank=True)
    data_criacao = models.DateTimeField(default=datetime.now, null=False, blank=False)
    categoria = models.CharField(max_length=1, choices=CATEGORIA_BASE, default='', null=False, blank=False)
    descriçao = models.TextField(max_length=300, null=False, blank=True)
    foto = models.ImageField(blank=True, upload_to='fotos/%Y/%m/%d/')
    mostrar = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
