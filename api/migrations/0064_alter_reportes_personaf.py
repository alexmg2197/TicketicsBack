# Generated by Django 4.2.6 on 2024-01-15 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0063_rename_personav_reportes_personaf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportes',
            name='PersonaF',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
