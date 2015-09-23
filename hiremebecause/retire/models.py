from django.db import models

# Create your models here.

class Parameters(models.Model):
    inflation = models.FloatField()

    def __str__(self):
        return self.inflation
