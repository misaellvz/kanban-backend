from rest_framework import serializers
from .models import Kanban

# Serializers define the API representation.
class KanbanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Kanban
        fields = ['created', 'title', 'description', 'asigned_to', 'status']