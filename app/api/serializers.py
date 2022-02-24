from rest_framework import serializers
from app.models import Task


class TaskSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(choices=('draft', 'done',
                                              'active', 'archived'))

    class Meta:
        model = Task
        fields = ('id', 'title', 'status')
