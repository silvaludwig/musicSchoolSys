from datetime import timedelta
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from django.conf import settings


def criar_evento_google_calendar(agendamento):
    creds = Credentials.from_authorized_user_file(
        "credentials.json", ["https://www.googleapis.com/auth/calendar"]
    )
    service = build("calendar", "v3", credentials=creds)

    event = {
        "summary": f"Aula de Música: {agendamento.aluno.nome}",
        "description": f"Aula com {agendamento.professor.nome}",
        "start": {
            "dateTime": agendamento.data_hora.isoformat(),
            "timeZone": "America/Sao_Paulo",
        },
        "end": {
            "dateTime": (agendamento.data_hora + timedelta(hours=1)).isoformat(),
            "timeZone": "America/Sao_Paulo",
        },
    }

    created_event = service.events().insert(calendarId="primary", body=event).execute()
    return created_event["id"]
