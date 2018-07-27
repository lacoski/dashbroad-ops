# Generated by Django 2.0.7 on 2018-07-27 06:59

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('keystone_user_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, django.contrib.auth.models.AnonymousUser),
        ),
    ]
