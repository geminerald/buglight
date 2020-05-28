from django.db import models

# Create your models here.


class Bug(models.Model):
    summary = models.CharField(max_length=254, default='')
    description = models.TextField()
    priority = models.IntegerField()

    def __str__(self):
        return self.summary
