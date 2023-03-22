from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'email',
        'sent_message',
        'sent_date',
        'sent_time',
    )


admin.site.register(Contact, ContactAdmin)
