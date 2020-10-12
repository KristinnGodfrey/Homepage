from django.db import models

# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=100)

    class Type(models.IntegerChoices):
        WEBDEV = 1
        SOFTWARE = 2
        DATABASE  = 3

    type = models.IntegerField(choices=Type.choices)

    def __str__(self):
        return self.name