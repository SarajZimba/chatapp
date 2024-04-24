# Generated by Django 5.0.3 on 2024-04-02 14:09

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('reset_token', models.CharField(default=uuid.uuid4, editable=False, max_length=1000)),
                ('reset_token_expiry', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
