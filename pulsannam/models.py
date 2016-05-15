from django.db import models

# Create your models here.


class IsrImage(models.Model):
    label = models.CharField(max_length=200)
    date  = models.DateTimeField('date published')


class IsrPlatform(models.Model):
    name = models.CharField(max_length=200)

class IsrPhase(models.Model):
    name = models.CharField(max_length=200)
    duration = models.IntegerField(default=0)
    label = models.ForeignKey(IsrImage)
    board = models.ForeignKey(IsrPlatform)
