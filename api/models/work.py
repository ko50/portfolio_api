from django.db import models
from django_mysql.models import ListCharField


class Work(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
    screenshot = models.ImageField(upload_to='works/', null=True)
    link = models.CharField(max_length=256)
    tags = ListCharField(
        models.CharField(max_length=15),
        size=15,
        max_length=(15 * 16)
    )

    def __str__(self):
        return self.name
