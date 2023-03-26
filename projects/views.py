from rest_framework import generics, permissions
from .models import Projects
from .serializers import ProjectSerializer
from developer_portofolio_backend.permissions import IsUserOrReadOnly


class ProjectsList(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Projects.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ProjectsDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsUserOrReadOnly]
    queryset = Projects.objects.all()
