from django.shortcuts import render

# Create your views here.
from .models import Skill

def index(request):
    skill_list = Skill.objects.all()
    context = {'skill_list': skill_list}
    return render(request, 'skills/index.html', context)