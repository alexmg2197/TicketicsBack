# Generated by Django 4.2.6 on 2023-11-02 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_rename_reporte_reportes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reportes',
            old_name='IdModulo',
            new_name='IdReporte',
        ),
    ]
