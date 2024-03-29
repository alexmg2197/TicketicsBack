# Generated by Django 4.2.6 on 2023-11-20 15:45

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0039_merge_20231120_0944'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicios',
            fields=[
                ('IdServicio', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Clave', models.CharField(max_length=500)),
                ('Servicio', models.CharField(max_length=100)),
                ('PersonaId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.personas')),
            ],
        ),
    ]
