# Generated by Django 3.2 on 2021-05-19 15:19

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='logo_path',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='contact',
            name='service_link',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='skill',
            name='logo_path',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='work',
            name='link',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='work',
            name='snapshot_path',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='work',
            name='tags',
            field=django_mysql.models.ListCharField(models.CharField(max_length=15), max_length=240, size=15),
        ),
    ]