from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    instrumento_principal = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Professor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    instrumentos = models.CharField(max_length=100)  # Ex: "Violão, Piano, Canto"

    def __str__(self):
        return self.nome
