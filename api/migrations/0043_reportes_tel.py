# Generated by Django 4.2.6 on 2023-11-22 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0042_merge_0040_servicios_0041_reportes_acciones'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportes',
            name='Tel',
            field=models.CharField(default='7711111111', max_length=12),
        ),
    ]
