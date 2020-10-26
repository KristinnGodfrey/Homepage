from django.db import models
import datetime


# Create your models here.
class Skill(models.Model):   
    name = models.CharField(max_length=100)

    class Type(models.IntegerChoices):
        WEBDEV = 1
        SOFTWARE = 2
        DATABASE  = 3

    type = models.IntegerField(choices=Type.choices)
    image = models.ImageField(null=True, blank=True, upload_to='img')

    def __str__(self):
        return self.name

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

class Project(models.Model):
    skill_id = models.ForeignKey(Skill, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True, upload_to='img')
    date = models.DateField('date of project')
    link = models.CharField(max_length=100)

    def __str__(self):
        return self.name