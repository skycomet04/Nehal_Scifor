# Generated by Django 4.2.4 on 2024-03-09 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_contact_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='timestamp',
        ),
    ]