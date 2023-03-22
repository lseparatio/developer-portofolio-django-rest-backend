from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = [
            'full_name', 'email', 'sent_message', 'sent_date', 'sent_time',
        ]
