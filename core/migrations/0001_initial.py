# Generated by Django 4.1.3 on 2023-02-02 04:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phoneNumber', models.CharField(max_length=15)),
                ('imageProfile', models.ImageField(blank=True, null=True, upload_to='images/profile')),
                ('departamento', models.CharField(max_length=20)),
                ('fechaIngreso', models.DateField(null=True)),
                ('estado', models.BooleanField(default=False)),
                ('direcion', models.CharField(max_length=50)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Attendence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(null=True)),
                ('turno', models.CharField(max_length=5, null=True)),
                ('horaInicio', models.TimeField(null=True)),
                ('horaFin', models.TimeField(null=True)),
                ('totalHoras', models.CharField(max_length=2)),
                ('attendenceProfile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.profile')),
            ],
        ),
    ]
