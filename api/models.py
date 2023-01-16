from django.db import models

# Create your models here.


class Qr(models.Model):
    link = models.CharField(max_length=255)
    holder = models.CharField(max_length=100)
    link_from = models.CharField(max_length=255)
    image = models.ImageField()
