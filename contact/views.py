from rest_framework.permissions import IsAdminUser
from django.http import Http404
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Contact
from .serializers import ContactSerializer
from developer_portofolio_backend.permissions import IsUserOrReadOnly
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail
# To do:
#  1, To allow get method only for admins


#       send_contact_email_to_us(name, email, sent_message)
#       send_contact_confirmation_email(name, email, sent_message)

class ContactMessages(APIView):
    serializer_class = ContactSerializer
    permission_classes = [IsAdminUser]

    def get(self, request):
        contact = Contact.objects.all()
        serializer = ContactSerializer(
            contact,    many=True, context={'request': request}
        )
        return Response(serializer.data)


class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ContactSerializer
    permission_classes = [IsAdminUser]
    queryset = Contact.objects.all()


class ContactForm(APIView):
    def post(self, request):
        serializer = ContactSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def send_contact_email_to_us(name, email, sent_message):
    """Send the content of contact form submision to admin"""
    email = email
    subject = render_to_string(
        'contact/confirmation_emails/send_contact_email_to_us_subject.txt',
        {'name': name})
    html_body = render_to_string(
        'contact/confirmation_emails/send_contact_email_to_us_body.html',
        {'name': name, 'email': email, 'sent_message': sent_message, 'contact_email': settings.DEFAULT_FROM_EMAIL})

    message = EmailMultiAlternatives(
        subject=subject,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[settings.DEFAULT_FROM_EMAIL]
    )
    message.attach_alternative(html_body, "text/html")
    message.send(fail_silently=False)


def send_contact_confirmation_email(name, email, sent_message):
    """Send the user contact form submision a confirmation email"""
    cust_email = email
    subject = render_to_string(
        'contact/confirmation_emails/send_contact_confirmation_email_subject.txt',
        {'name': name})
    html_body = render_to_string(
        'contact/confirmation_emails/send_contact_confirmation_email_body.html',
        {'name': name, 'email': email, 'sent_message': sent_message, 'contact_email': settings.DEFAULT_FROM_EMAIL})

    message = EmailMultiAlternatives(
        subject=subject,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[cust_email]
    )
    message.attach_alternative(html_body, "text/html")
    message.send(fail_silently=False)
