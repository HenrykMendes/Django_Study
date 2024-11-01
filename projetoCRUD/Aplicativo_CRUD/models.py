from django.db import models

# Create your models here.
class item (models.Model):
    #Campos que vão ser criados do database
    nome = models.CharField (max_length=100)
    descricao = models.TextField
    preco = models.DecimalField (max_digits=10, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)