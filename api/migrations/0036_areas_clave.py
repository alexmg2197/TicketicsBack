# Generated by Django 4.2.6 on 2023-11-15 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0035_alter_reportes_fechaf'),
    ]

    operations = [
        migrations.AddField(
            model_name='areas',
            name='Clave',
            field=models.CharField(default='ccc', max_length=3),
        ),
    ]
