# Generated by Django 4.2.7 on 2023-11-15 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0035_alter_reportes_fechaf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportes',
            name='Folio',
            field=models.CharField(max_length=12),
        ),
    ]
