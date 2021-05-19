from django.db import models


class AboutMeInformation(models.Model):
    title = models.CharField(max_length=8)
    content = models.CharField(max_length=32)

    def __str__(self):
        return self.title
