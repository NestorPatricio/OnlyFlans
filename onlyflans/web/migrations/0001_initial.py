# Generated by Django 3.2.4 on 2022-03-21 21:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flan',
            fields=[
                ('flan_uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('image_url', models.URLField()),
                ('slug', models.SlugField(allow_unicode=True)),
                ('is_private', models.BooleanField()),
            ],
        ),
    ]
