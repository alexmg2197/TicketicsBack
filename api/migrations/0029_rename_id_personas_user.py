# Generated by Django 4.2.6 on 2023-11-04 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0028_rename_per_personas_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personas',
            old_name='id',
            new_name='user',
        ),
    ]
