# Generated by Django 4.2.6 on 2024-01-17 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0066_alter_reportes_contf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportes',
            name='ContF',
            field=models.IntegerField(blank=True, max_length=4, null=True),
        ),
    ]
