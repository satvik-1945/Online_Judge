from django.db import models

# Create your models here.
class problem(models.Model):
    name = models.CharField(max_length=500)
    desc = models.TextField()
    difficulty = models.CharField(max_length=200)