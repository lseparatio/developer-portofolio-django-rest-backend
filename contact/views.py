from django.http import Http404
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Contact
from .serializers import ContactSerializer
from developer_portofolio_backend.permissions import IsUserOrReadOnly
from django.core.mail import send_mail
# To do:
#  1, To allow get method only for admins
#  2, To actualy send custom  html mails


class ContactList(generics.ListCreateAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()

    def perform_create(self, serializer):
        name = serializer.validated_data['full_name']
        email = serializer.validated_data['email']
        sent_message = serializer.validated_data['sent_message']
        send_message(name, email, sent_message)
        send_confirmation(name, email, sent_message)

        serializer.save()


def send_message(name, email, sent_message):
    send_mail(
        email,
        sent_message,
        'contact@ionutzapototchi.com',
        ['test@ionutzapototchi.com'],
        fail_silently=False,
    )


def send_confirmation(name, email, sent_message):
    send_mail(
        'We got your message',
        'We got your message and we will reply soon',
        'contact@ionutzapototchi.com',
        [email],
        fail_silently=False,
    )
