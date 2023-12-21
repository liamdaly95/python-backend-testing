from django.db import models

class Locations(models.Model):
    city = models.CharField(max_length=60)
    country = models.CharField(max_length=60)

def __str__(self):
        return self.city
