from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=32)
    user_name = models.CharField(max_length=32)
    service_link = models.CharField(max_length=128)
    logo_path = models.CharField(max_length=128)

    def __str__(self):
        return self.name
