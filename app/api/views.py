from rest_framework import viewsets
from .serializers import TaskSerializer
from app.models import Task
from rest_framework.decorators import action
from rest_framework.response import Response


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @action(detail=True, methods=['POST'])
    def change_status(self, request, **args):
        workflow = ['draft', 'done', 'active', 'archived']
        obj = Task.objects.get(pk=args['pk'])
        status = request.POST['status']
        if status in workflow:
            ind1 = workflow.index(status)
            ind2 = workflow.index(obj.status)
            if status == obj.status:
                return Response({'status': 'the same status'})
            elif (ind1 > ind2 and abs(ind1 - ind2) == 1) or status == 'archived':
                obj.status = status
                obj.save()
                return Response({'status': 'action done'})
            else:
                return Response({'status': 'error in workflow'})
        else:
            return Response({'status': 'error in workflow'})
