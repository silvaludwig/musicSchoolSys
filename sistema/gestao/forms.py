from django import forms
from .models import Aluno, Aula
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import DateInput


class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ["nome", "idade"]


class AulaForm(forms.ModelForm):
    repetir_semanalmente = forms.BooleanField(
        required=False, label="Repetir semanalmente"
    )
    semanas_repeticao = forms.IntegerField(
        required=False, min_value=1, max_value=52, label="Por quantas semanas?"
    )

    data = forms.DateField(
        input_formats=["%d/%m/%Y"],
        widget=DateInput(
            format="%d/%m/%Y",
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "dd/mm/aaaa",
            },
        ),
        label="Data",
    )

    class Meta:
        model = Aula
        fields = ["instrumento", "data", "horario", "aluno"]
        exclude = ["professor", "data_cadastro"]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        super().__init__(*args, **kwargs)
        self.fields["aluno"].queryset = user.alunos.all()


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
