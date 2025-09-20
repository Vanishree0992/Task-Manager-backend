from rest_framework import viewsets, filters
from .models import Task
from .serializers import TaskSerializer
from rest_framework.permissions import AllowAny

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer
    permission_classes = [AllowAny]  # No auth for now

    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']

    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.query_params.get('status')
        if status == 'completed':
            queryset = queryset.filter(is_completed=True)
        elif status == 'active':
            queryset = queryset.filter(is_completed=False)
        return queryset
