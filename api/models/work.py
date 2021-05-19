from django.db import models
from django_mysql.models import ListCharField


class Work(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
    snapshot_path = models.CharField(max_length=128)
    link = models.CharField(max_length=256)
    tags = ListCharField(
        models.CharField(max_length=15),
        size=15,
        max_length=(15 * 16)
    )
