from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_at',
        'birth_date',
        'phone_number',
        'street_address1',
        'street_address2',
        'town_or_city',
        'county',
        'postcode',
        'country',
    )

admin.site.register(Profile, ProfileAdmin)