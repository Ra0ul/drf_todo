# Generated by Django 4.2 on 2023-04-30 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
    ]
