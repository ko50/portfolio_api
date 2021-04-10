from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=8)
    user_name = models.CharField(max_length=32)
    service_link = models.CharField(max_length=64)
    logo_path = models.TextField()
