# Generated by Django 4.2.6 on 2024-01-15 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0061_reportes_personav'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportes',
            name='PersonaV',
            field=models.CharField(max_length=250),
        ),
    ]