from django.db import models


class Teacher(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)
    instrumento = models.CharField(max_length=50)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
