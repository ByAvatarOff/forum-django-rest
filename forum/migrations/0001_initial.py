# Generated by Django 3.0.5 on 2020-12-22 16:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('slug', models.SlugField(unique=True, verbose_name='url')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')),
                ('published', models.BooleanField()),
                ('views', models.IntegerField(default=0, verbose_name='Просмотры')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.Category')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='LikeDislike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField()),
                ('dislike', models.BooleanField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.Posts')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.Posts')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
