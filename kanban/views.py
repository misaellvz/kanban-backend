from .models import Kanban
from rest_framework import viewsets
from .serializers import KanbanSerializer

# ViewSets define the view behavior.
class KanbanViewSet(viewsets.ModelViewSet):
    queryset = Kanban.objects.all()
    serializer_class = KanbanSerializer