from django.shortcuts import render, redirect, get_object_or_404
from .models import Aluno, Professor
from .forms import AlunoForm, ProfessorForm
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required, user_passes_test


def index(request):
    return render(request, "gestao/index.html")


# Verifica se o usuário é admin
def is_admin(user):
    return user.is_authenticated and user.is_superuser


# Proteja as views com login_required
@login_required
@user_passes_test(is_admin)
def lista_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, "gestao/lista_alunos.html", {"alunos": alunos})


# Protege a view com login_required + user_passes_test (só admin acessa)
@login_required
@user_passes_test(is_admin, login_url="index")  # Redireciona não-admins para a homepage
def novo_aluno(request):
    ultimos_alunos = Aluno.objects.order_by("-data_cadastro")[:5]

    if request.method == "POST":
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Aluno cadastrado com sucesso!"
            )  # Mensagem de confirmação
            return redirect("lista_alunos")
    else:
        form = AlunoForm()

    return render(
        request,
        "gestao/novo_aluno.html",
        {
            "form": form,
            "ultimos_alunos": ultimos_alunos,
        },
    )


@login_required
@user_passes_test(is_admin)
def editar_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    if request.method == "POST":
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect("lista_alunos")
    else:
        form = AlunoForm(instance=aluno)
    return render(request, "gestao/form_aluno.html", {"form": form})


@login_required
@user_passes_test(is_admin)
def deletar_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    if request.method == "POST":
        aluno.delete()
        return redirect("lista_alunos")
    return render(request, "gestao/confirmar_delete.html", {"aluno": aluno})


# VIEWS PROFESSOR
# Proteja as views com login_required
@login_required
@user_passes_test(is_admin)
def lista_professores(request):
    professores = Professor.objects.all()
    return render(
        request, "gestao/lista_professores.html", {"professores": professores}
    )


# Protege a view com login_required + user_passes_test (só admin acessa)
@login_required
@user_passes_test(is_admin, login_url="index")  # Redireciona não-admins para a homepage
def novo_professor(request):
    ultimos_professores = Professor.objects.order_by("-data_cadastro")[:5]

    if request.method == "POST":
        form = ProfessorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Professor cadastrado com sucesso!"
            )  # Mensagem de confirmação
            return redirect("lista_professores")
    else:
        form = ProfessorForm()

    return render(
        request,
        "gestao/novo_professor.html",
        {
            "form": form,
            "ultimos_professores": ultimos_professores,
        },
    )


@login_required
@user_passes_test(is_admin)
def editar_professor(request, id):
    professor = get_object_or_404(Professor, id=id)
    if request.method == "POST":
        form = ProfessorForm(request.POST, instance=professor)
        if form.is_valid():
            form.save()
            return redirect("lista_professores")
    else:
        form = ProfessorForm(instance=professor)
    return render(request, "gestao/form_professor.html", {"form": form})


@login_required
@user_passes_test(is_admin)
def deletar_professor(request, id):
    professor = get_object_or_404(Professor, id=id)
    if request.method == "POST":
        professor.delete()
        return redirect("lista_professores")
    return render(request, "gestao/confirmar_delete.html", {"professor": professor})
