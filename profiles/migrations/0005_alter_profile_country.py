# Generated by Django 4.1.2 on 2022-11-10 08:38

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_alter_profile_options_profile_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=django_countries.fields.CountryField(blank=True, default='null', max_length=2, null=True),
        ),
    ]