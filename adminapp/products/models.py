from django.db import models

# Create your models here.
class Product(models.Model):
    objects = models.Manager()
    image = models.CharField(max_length=300)
    title = models.CharField(max_length=300)
    likes = models.PositiveIntegerField(default=0)

class User(models.Model):
    objects = models.Manager()
    pass