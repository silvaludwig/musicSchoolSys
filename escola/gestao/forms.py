from django import forms
from .models import Aluno, Professor
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ["nome", "email", "telefone", "instrumento_principal"]


class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ["nome", "email", "telefone", "instrumentos"]


class CadastroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.is_staff = False  # Garante que não seja staff
        user.is_superuser = False  # Garante que não seja superusuário
        if commit:
            user.save()
        return user
