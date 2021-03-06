# Generated by Django 3.2 on 2021-04-08 11:07

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMeInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=8)),
                ('content', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=8)),
                ('user_name', models.CharField(max_length=32)),
                ('service_link', models.CharField(max_length=64)),
                ('logo_path', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=8)),
                ('description', models.TextField()),
                ('logo_path', models.TextField()),
                ('skill_type', models.CharField(choices=[('Languages', 'Languages'), ('Frameworks', 'Frameworks'), ('Tools', 'Tools')], max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('description', models.TextField()),
                ('snapshot_path', models.TextField()),
                ('link', models.TextField()),
                ('tags', django_mysql.models.ListCharField(models.CharField(max_length=10), max_length=120, size=10)),
            ],
        ),
    ]
