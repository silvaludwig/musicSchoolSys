from django import forms
from .models import Aluno, Professor


class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ["nome", "email", "telefone", "instrumento_principal"]


class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ["nome", "email", "telefone", "instrumentos"]
