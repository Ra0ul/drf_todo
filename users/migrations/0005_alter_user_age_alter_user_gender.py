# Generated by Django 4.2 on 2023-04-27 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_age_alter_user_gender_alter_user_intro_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.PositiveSmallIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[(None, '선택'), ('M', '남성'), ('W', '여성'), ('N', '선택하지 않음')], default='N', max_length=7),
        ),
    ]
