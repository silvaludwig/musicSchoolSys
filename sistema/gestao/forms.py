from django import forms
from .models import Aluno, Aula
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ["nome", "idade", "professor"]


class AulaForm(forms.ModelForm):
    class Meta:
        model = Aula
        fields = ["titulo", "data", "horario", "professor", "aluno"]


class CadastroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.is_superuser = True  # Garante que seja superusuário
        if commit:
            user.save()
        return user
