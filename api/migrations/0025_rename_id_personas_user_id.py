# Generated by Django 4.2.6 on 2023-11-03 23:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_rename_user_personas_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personas',
            old_name='id',
            new_name='user_id',
        ),
    ]
