from django.contrib.auth.decorators import login_required
from .models import Aula, Aluno
from django.shortcuts import render, redirect, get_object_or_404
from .forms import AlunoForm, AulaForm, CadastroUsuarioForm
from django.contrib.auth import login
from datetime import timedelta
from django.http import JsonResponse


@login_required
def dashboard(request):
    total_alunos = Aluno.objects.filter(professor=request.user).count()
    total_aulas = Aula.objects.filter(professor=request.user).count()
    return render(
        request,
        "gestao/dashboard.html",
        {
            "total_alunos": total_alunos,
            "total_aulas": total_aulas,
        },
    )


@login_required
def meus_alunos(request):
    alunos = Aluno.objects.filter(professor=request.user)
    return render(request, "gestao/alunos.html", {"alunos": alunos})


@login_required
def novo_aluno(request):
    if request.method == "POST":
        form = AlunoForm(request.POST)
        if form.is_valid():
            aluno = form.save(commit=False)
            aluno.professor = request.user
            aluno.save()
            return redirect("meus_alunos")
    else:
        form = AlunoForm()
    return render(request, "gestao/novo_aluno.html", {"form": form})


@login_required
def index(request):
    # Contagem de registros para mostrar no dashboard
    total_alunos = Aluno.objects.filter(professor=request.user).count()
    total_aulas = Aula.objects.filter(professor=request.user).count()

    context = {
        "total_aulas": total_aulas,
        "total_alunos": total_alunos,
    }
    return render(request, "gestao/index.html", context)


@login_required
def editar_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    if request.method == "POST":
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect("alunos")
    else:
        form = AlunoForm(instance=aluno)
    return render(request, "gestao/form_aluno.html", {"form": form})


@login_required
def deletar_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    if request.method == "POST":
        aluno.delete()
        return redirect("meus_alunos")
    return render(request, "gestao/confirmar_delete.html", {"aluno": aluno})


@login_required
def minhas_aulas(request):
    aulas = Aula.objects.filter(professor=request.user)
    return render(request, "gestao/aulas.html", {"aulas": aulas})


@login_required
def nova_aula(request):
    if request.method == "POST":
        form = AulaForm(request.POST, user=request.user)  # <-- Aqui
        if form.is_valid():
            repetir = form.cleaned_data.get("repetir_semanalmente", False)
            semanas = form.cleaned_data.get("semanas_repeticao", 1)
            aula_base = form.save(commit=False)
            aula_base.professor = request.user
            aula_base.save()

            if repetir and semanas > 1:
                for i in range(1, semanas):
                    nova_data = aula_base.data + timedelta(weeks=i)
                    Aula.objects.create(
                        instrumento=aula_base.instrumento,
                        aluno=aula_base.aluno,
                        data=nova_data,
                        horario=aula_base.horario,
                        professor=request.user,
                    )
            return redirect("minhas_aulas")
    else:
        form = AulaForm(user=request.user)  # <-- Aqui também

    ultimas_aulas = Aula.objects.filter(professor=request.user).order_by(
        "-data_cadastro"
    )[:5]
    return render(
        request, "gestao/nova_aula.html", {"form": form, "ultimas_aulas": ultimas_aulas}
    )


@login_required
def editar_aula(request, id):
    aula = get_object_or_404(Aula, id=id)
    if request.method == "POST":
        form = AulaForm(request.POST, instance=aula)
        if form.is_valid():
            form.save()
            return redirect("minhas_aulas")
    else:
        form = AulaForm(instance=aula)
    return render(request, "gestao/form_aula.html", {"form": form})


@login_required
def deletar_aula(request, id):
    aula = get_object_or_404(Aula, id=id)
    if request.method == "POST":
        aula.delete()
        return redirect("minhas_aulas")
    return render(request, "gestao/confirmar_delete.html", {"aula": aula})


def cadastro_usuario(request):
    if request.method == "POST":
        form = CadastroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Loga o usuário automaticamente após o cadastro
            return redirect(
                "index"
            )  # Substitua pelo nome da sua URL de redirecionamento
    else:
        form = CadastroUsuarioForm()
    return render(request, "gestao/cadastro_usuario.html", {"form": form})


@login_required
def eventos_aulas(request):
    aulas = Aula.objects.filter(professor=request.user)
    eventos = []

    for aula in aulas:
        eventos.append(
            {
                "title": f"{aula.instrumento} - {aula.aluno.nome}",
                "start": f"{aula.data}T{aula.horario}",
            }
        )

    return JsonResponse(eventos, safe=False)


@login_required
def calendario(request):
    return render(request, "gestao/calendario.html")
