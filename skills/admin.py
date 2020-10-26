from django.contrib import admin

# Register your models here.
from .models import Skill, Project

admin.site.register(Skill)
admin.site.register(Project)