from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Aluno(models.Model):
    nome = models.CharField(max_length=50)
    data_nascimento = models.DateField()
    email = models.CharField(max_length=50)
    telefone = models.IntegerField(null=False)
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
        return f"Aula de {self.instrumento} | {self.data}, {self.horario}"


class Pagamento(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    data_pagamento = models.DateField(default=date.today)
    referente_ao_mes = models.CharField(
        max_length=20,
    )
    foi_pago = models.BooleanField(default=True)
    forma_pagamento = models.CharField(
        max_length=20,
        choices=[
            ("dinheiro", "Dinheiro"),
            ("pix", "PIX"),
            ("transferencia", "Transferência"),
            ("boleto", "Boleto"),
            ("outro", "Outro"),
        ],
        default="pix",
    )

    def __str__(self):
        return f"{self.aluno.nome} - {self.referente_ao_mes}"
