from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=32)
    user_name = models.CharField(max_length=32)
    service_link = models.CharField(max_length=128)
    logo = models.FileField(upload_to='contacts/', null=True)

    def __str__(self):
        return self.name
