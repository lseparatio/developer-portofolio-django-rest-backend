from django.http import Http404
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Contact
from .serializers import ContactSerializer
from developer_portofolio_backend.permissions import IsUserOrReadOnly


class ContactList(generics.ListCreateAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()

    def perform_create(self, serializer):
        serializer.save()


class ProfileDetail(APIView):
    serializer_class = ContactSerializer
    permission_classes = [IsUserOrReadOnly]

    def get_object(self, pk):
        try:
            contact = Contact.objects.get(pk=pk)
            self.check_object_permissions(self.request, contact)
            return contact
        except Contact.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        contact = self.get_object(pk)
        serializer = ContactSerializer(
            contact, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        contact = self.get_object(pk)
        serializer = ContactSerializer(
            contact, data=request.data, context={'request': request}
        )
