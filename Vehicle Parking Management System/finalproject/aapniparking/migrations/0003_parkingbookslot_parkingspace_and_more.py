# Generated by Django 4.2.4 on 2024-04-15 08:06

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aapniparking', '0002_parkingslot_delete_parking'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParkingBookSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('veh_model', models.CharField(max_length=255)),
                ('veh_registration', models.CharField(max_length=10)),
                ('owner_contactno', models.CharField(max_length=10)),
                ('parking_rate', models.PositiveIntegerField()),
                ('intime', models.DateTimeField(auto_now_add=True)),
                ('outtime', models.DateTimeField(blank=True, null=True)),
                ('fee', models.FloatField()),
                ('vehicle_type', models.CharField(choices=[('4', '4-wheeler'), ('3', '3-wheeler'), ('2', '2-wheeler')], default='2', max_length=50)),
                ('booking_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ParkingSpace',
            fields=[
                ('no', models.BigAutoField(primary_key=True, serialize=False, unique=True)),
                ('veh_type', models.CharField(choices=[('4', '4-wheeler'), ('3', '3-wheeler'), ('2', '2-wheeler')], max_length=255)),
                ('is_available', models.BooleanField(default=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='owner_name',
        ),
        migrations.AddField(
            model_name='vehicle',
            name='created_by',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='owner',
            field=models.CharField(default='dev', max_length=200),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='contact',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '9999999999'. Up to 10 digits allowed.", regex='^[6-9]\\d{9}$')]),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='vehicle_category',
            field=models.CharField(choices=[('4', '4-wheeler'), ('3', '3-wheeler'), ('2', '2-wheeler')], default='2', max_length=50),
        ),
        migrations.DeleteModel(
            name='ParkingSlot',
        ),
        migrations.AddField(
            model_name='parkingbookslot',
            name='owner_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicle_owner', to='aapniparking.vehicle'),
        ),
        migrations.AddField(
            model_name='parkingbookslot',
            name='slot_no',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='aapniparking.parkingspace'),
        ),
        migrations.AddField(
            model_name='parkingbookslot',
            name='vehicle_uniqueid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vehicle_uniqueid', to='aapniparking.vehicle'),
        ),
    ]
