# Generated by Django 4.2 on 2023-05-04 12:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='completion_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='완료 시간'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='생성 시간'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='is_complete',
            field=models.BooleanField(default=False, verbose_name='완료 여부'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(max_length=50, verbose_name='할일 제목'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='수정 시간'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='작성자'),
        ),
    ]
