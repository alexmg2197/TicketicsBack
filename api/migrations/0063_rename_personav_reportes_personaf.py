# Generated by Django 4.2.6 on 2024-01-15 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0062_alter_reportes_personav'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reportes',
            old_name='PersonaV',
            new_name='PersonaF',
        ),
    ]
