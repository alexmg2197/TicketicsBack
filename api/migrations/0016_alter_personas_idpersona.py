# Generated by Django 4.2.6 on 2023-11-03 23:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_rename_user_id_personas_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personas',
            name='IdPersona',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
