from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path("", views.index, name="index"),  # Homepage
    path("alunos/", views.lista_alunos, name="lista_alunos"),
    path("alunos/novo/", views.novo_aluno, name="novo_aluno"),
    path("alunos/editar/<int:id>/", views.editar_aluno, name="editar_aluno"),
    path("alunos/deletar/<int:id>/", views.deletar_aluno, name="deletar_aluno"),
    path("professores/", views.lista_professores, name="lista_professores"),
    path("professores/novo/", views.novo_professor, name="novo_professor"),
    path(
        "professores/editar/<int:id>/", views.editar_professor, name="editar_professor"
    ),
    path(
        "professores/deletar/<int:id>/",
        views.deletar_professor,
        name="deletar_professor",
    ),
    path("login/", LoginView.as_view(template_name="gestao/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
