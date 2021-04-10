from django.db import models
from django_mysql.models import ListCharField


class Work(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
    snapshot_path = models.TextField()
    link = models.TextField()
    tags = ListCharField(
        models.CharField(max_length=10),
        size=10,
        max_length=120
    )
