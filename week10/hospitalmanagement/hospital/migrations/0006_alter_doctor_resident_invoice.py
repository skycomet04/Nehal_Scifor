# Generated by Django 4.2.4 on 2024-04-27 03:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0005_alter_appointment_doc_fee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='resident',
            field=models.TextField(default='-'),
        ),
        migrations.CreateModel(
            name='invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('treating_doctor', models.CharField(max_length=255)),
                ('patient_name', models.CharField(max_length=255)),
                ('department', models.CharField(max_length=255)),
                ('amount', models.PositiveIntegerField()),
                ('qty', models.PositiveIntegerField()),
                ('services', models.TextField()),
                ('admit_date', models.DateField(blank=True, null=True)),
                ('discharge_date', models.DateField(blank=True, null=True)),
                ('address', models.CharField(max_length=250)),
                ('mobile', models.IntegerField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=150)),
                ('bill_date', models.DateTimeField(auto_now_add=True)),
                ('total_amount', models.PositiveIntegerField()),
                ('remarks', models.TextField(blank=True, null=True)),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.appointment')),
            ],
        ),
    ]