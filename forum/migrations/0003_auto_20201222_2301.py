# Generated by Django 3.0.5 on 2020-12-22 20:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0002_remove_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='author',
            field=models.CharField(max_length=140, null=True),
        ),
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='posts',
            name='author',
            field=models.CharField(max_length=140, null=True),
        ),
    ]
