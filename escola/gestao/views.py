from django.shortcuts import render, redirect, get_object_or_404
from .models import Aluno
from .forms import AlunoForm
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required, user_passes_test


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


def index(request):
    return render(request, "gestao/index.html")


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
