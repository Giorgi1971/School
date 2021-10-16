from django.db import models

# Create your models here.


class Subject(models.IntegerChoices):
    PHYSIC = 1
    MUSIC = 2
    CHEMYSTRY = 3


class Room(models.Model):
    number = models.PositiveSmallIntegerField()