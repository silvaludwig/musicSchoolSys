from rest_framework import viewsets
from .models import Scheduling
from .serializers import SchedulingSerializer


class SchedulingViewSet(viewsets.ModelViewSet):
    queryset = Scheduling.objects.all()
    serializer_class = SchedulingSerializer
