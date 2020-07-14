# Generated by Django 2.2.11 on 2020-06-02 13:42

import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0052_remove_user_avatar_hash'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='roles',
        ),
        migrations.AddField(
            model_name='user',
            name='roles',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.BigIntegerField(validators=[django.core.validators.MinValueValidator(limit_value=0, message='Role IDs cannot be negative.')]), default=list, help_text='IDs of roles the user has on the server', size=None),
        ),
    ]
