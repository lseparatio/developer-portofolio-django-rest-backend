from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Projects
from .serializers import ProjectSerializer
from developer_portofolio_backend.permissions import IsUserOrReadOnly


class ProjectsList(APIView):
    def get(self, request):
        projects = Projects.objects.all()
        serializer = ProjectSerializer(
            projects, many=True, context= {'request': request }
        )   
        return Response(serializer.data)


class ProjectsDetail(APIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsUserOrReadOnly]

    def get_object(self, pk):
        try:
            project = Projects.objects.get(pk=pk)
            self.check_object_permissions(self.request, project)
            return project
        except Projects.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectSerializer(
            project, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectSerializer(
            project, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
