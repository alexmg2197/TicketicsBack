# Generated by Django 4.2.6 on 2023-11-27 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0057_alter_reportes_horaf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportes',
            name='FechaF',
            field=models.DateField(blank=True, null=True),
        ),
    ]
