# Generated by Django 4.2.9 on 2024-01-03 10:23

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(old_name="UserProfile", new_name="Profile",),
    ]
