# Generated by Django 4.2.6 on 2023-11-22 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0047_rename_tel_reportes_nt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reportes',
            name='nT',
        ),
        migrations.AddField(
            model_name='reportes',
            name='Tel',
            field=models.CharField(default='7711111111', max_length=12),
        ),
    ]
