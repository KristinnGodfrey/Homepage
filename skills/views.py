from django.shortcuts import render

# Create your views here.
from .models import Skill, Project


def index(request):
    skill_list = Skill.objects.all()
    context = { 'webdev': skill_list.filter(type=1),
                'software': skill_list.filter(type=2),
                'database': skill_list.filter(type=3)
    }
    return render(request, 'skills/index.html', context)

def projects(request):
    project_list = Project.objects.all()
    context = {'projects': project_list}
    return render(request, 'skills/index.html', context)