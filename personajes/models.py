from django.db import models

# Create your models here.

class Bueno (models.Model):
    nombre = models.CharField(max_length=65)
    sexo = models.CharField(max_length=9)
    anime = models.CharField(max_length=65)
    bio = models.TextField()


class Malo (models.Model):
    nombre = models.CharField(max_length=65)
    sexo = models.CharField(max_length=9)
    anime = models.CharField(max_length=65)
    bio = models.TextField()

class Neutral (models.Model):
    nombre = models.CharField(max_length=65)
    sexo = models.CharField(max_length=9)
    anime = models.CharField(max_length=65)
    bio = models.TextField()

class Total (models.Model):
    nombre = models.CharField(max_length=65)
    sexo = models.CharField(max_length=9)
    anime = models.CharField(max_length=65)
    bio = models.TextField()