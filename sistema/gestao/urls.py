from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import cadastro_usuario

urlpatterns = [
    path("", views.index, name="index"),
    path("alunos/", views.meus_alunos, name="meus_alunos"),
    path("alunos/novo/", views.novo_aluno, name="novo_aluno"),
    path("alunos/editar/<int:id>/", views.editar_aluno, name="editar_aluno"),
    path("alunos/deletar/<int:id>/", views.deletar_aluno, name="deletar_aluno"),
    path("aulas/", views.minhas_aulas, name="minhas_aulas"),
    path("aulas/novo/", views.nova_aula, name="nova_aula"),
    path("aulas/editar/<int:id>/", views.editar_aula, name="editar_aula"),
    path("aulas/deletar/<int:id>/", views.deletar_aula, name="deletar_aula"),
    path("accounts/login/", auth_views.LoginView.as_view(), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("cadastro/", cadastro_usuario, name="cadastro_usuario"),
    path("calendario/", views.calendario, name="calendario"),
    path("eventos/", views.eventos_aulas, name="eventos_aulas"),
    path("novo_pagamento/", views.novo_pagamento, name="novo_pagamento"),
    path("financeiro/", views.resumo_financeiro, name="resumo_financeiro"),
]
