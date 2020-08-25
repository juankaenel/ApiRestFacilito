# Generated by Django 3.1 on 2020-08-25 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=50)),
                ('slug', models.SlugField()),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Video',
                'verbose_name_plural': 'Videos',
                'db_table': 'video',
                'ordering': ['id'],
            },
        ),
    ]