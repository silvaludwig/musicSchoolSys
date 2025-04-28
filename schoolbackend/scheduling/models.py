from django.db import models

from students.models import Student
from teachers.models import Teacher


class Scheduling(models.Model):
    aluno = models.ForeignKey(Student, on_delete=models.CASCADE)
    professor = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()
    confirmado = models.BooleanField(default=False)
    google_calendar_event_id = models.CharField(
        max_length=100, blank=True
    )  # Para armazenar o ID do evento no Google Agenda

    def __str__(self):
        return f"Aula de {self.aluno} com {self.professor} em {self.data_hora}"
