from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    goals = Goal.objects.all()
    return render(request, 'targets/index.html',{'goals':goals})