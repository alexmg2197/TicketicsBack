# Generated by Django 4.2.6 on 2023-11-22 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0051_rename_cel_reportes_contacto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportes',
            name='Contacto',
            field=models.CharField(default='cccccccccc', max_length=12),
        ),
    ]
