# Generated by Django 4.2.6 on 2023-11-03 23:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_personas_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personas',
            old_name='user',
            new_name='id',
        ),
    ]
