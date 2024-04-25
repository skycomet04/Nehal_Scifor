# Generated by Django 4.2.4 on 2024-04-18 06:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aapniparking', '0004_parkingbookslot_parking_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parkingbookslot',
            name='owner_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]