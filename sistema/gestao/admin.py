from django.contrib import admin
from .models import Aluno, Aula
from .models import Pagamento

admin.site.register(Aluno)
admin.site.register(Aula)


@admin.register(Pagamento)
class PagamentoAdmin(admin.ModelAdmin):
    list_display = [
        "aluno",
        "referente_ao_mes",
        "valor",
        "forma_pagamento",
        "data_pagamento",
        "foi_pago",
    ]
    list_filter = ["forma_pagamento", "foi_pago"]
    search_fields = ["aluno__nome", "referente_ao_mes"]
    pagamentos_hoje = Pagamento.objects.all()
