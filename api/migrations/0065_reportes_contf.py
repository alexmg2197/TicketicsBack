# Generated by Django 4.2.6 on 2024-01-17 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0064_alter_reportes_personaf'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportes',
            name='ContF',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
