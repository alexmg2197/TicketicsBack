# Generated by Django 4.2.7 on 2023-11-14 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0033_alter_reportes_fechai'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportes',
            name='FechaI',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]