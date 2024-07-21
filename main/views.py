from rest_framework import generics, viewsets
from rest_framework.exceptions import PermissionDenied

from .models import Task, Tag
from .serializers import TaskSerializer, TagSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_object(self):
        obj = super().get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return obj


class SharedTaskDetail(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_object(self):
        return Task.objects.get(uuid=self.kwargs['uuid'])


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagList(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TaskSearch(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        title = self.request.query_params.get('title')
        tag = self.request.query_params.get('tag')
        queryset = Task.objects.filter(author=self.request.user)
        if title:
            queryset = queryset.filter(title__icontains=title)
        if tag:
            queryset = queryset.filter(tags__name__icontains=tag)
        return queryset
