from cgitb import html
from django.shortcuts import render, HttpResponse
from Home.models import team

# all_objects = team.objects.all()
# Create your views here.
def index(request):
    all_objects = team.objects.all()
    return render(request, 'index.html', {"all_objects":all_objects})
    
def teams(request, teamId): 
    new = team.objects.all().filter(teamId = teamId)
    return render(request, 'base.html', {'all_objects':new})

