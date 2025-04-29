from django.contrib import admin
from .models import Aluno, Professor


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "instrumento_principal")
    search_fields = ("nome", "email")


admin.site.register(Professor)
