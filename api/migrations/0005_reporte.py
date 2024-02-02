# Generated by Django 4.2.6 on 2023-11-02 16:19

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rename_iddistrito_agencias_distritoid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reporte',
            fields=[
                ('IdModulo', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Folio', models.IntegerField()),
                ('FechaI', models.DateTimeField()),
                ('FechaF', models.DateTimeField()),
                ('Prioridad', models.CharField(max_length=20)),
                ('PersonaS', models.CharField(max_length=250)),
                ('Estatus', models.CharField(max_length=20)),
                ('ModuloId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.modulos')),
                ('PersonaId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.personas')),
            ],
        ),
    ]
