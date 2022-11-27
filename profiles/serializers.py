from rest_framework import serializers
from .models import Profile
from django_countries.serializers import CountryFieldMixin


class ProfileSerializer(CountryFieldMixin, serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    is_user = serializers.SerializerMethodField()

    def get_is_user(self, obj):
        request = self.context['request']
        return request.user == obj.user

    class Meta:
        model = Profile
        fields = [
            'id', 'user', 'birth_date', 'phone_number', 'street_address1',
            'street_address2', 'town_or_city', 'county', 'postcode', 'country', 'is_user', 'image',
        ]
