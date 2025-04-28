from rest_framework import viewsets
from .models import Teacher
from .serializers import teacherSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = teacherSerializer
