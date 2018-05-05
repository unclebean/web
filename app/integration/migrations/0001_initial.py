# Generated by Django 2.0.5 on 2018-05-05 19:27

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import economy.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dashboard', '0066_auto_20180505_1928'),
    ]

    operations = [
        migrations.CreateModel(
            name='Integration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('name', models.CharField(max_length=255)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='name')),
                ('config', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='integrations', to='dashboard.Profile')),
            ],
            options={
                'ordering': ('-created_on',),
            },
        ),
    ]