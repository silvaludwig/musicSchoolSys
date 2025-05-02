from django.db import models
from django.contrib.auth.models import User


class Aluno(models.Model):
    nome = models.CharField(max_length=50)
    data_nascimento = models.DateField()
    email = models.CharField(max_length=50)
    telefone = models.IntegerField(max_length=15, null=False)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    professor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="alunos")

    def __str__(self):
        return self.nome


class Aula(models.Model):
    instrumento = models.CharField(max_length=50)
    data = models.DateField()
    horario = models.TimeField()
    data_cadastro = models.DateTimeField(auto_now_add=True)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name="aulas")
    professor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="aulas")

    def __str__(self):
        return f"Aula de {self.titulo} | {self.data}, {self.horario}"
