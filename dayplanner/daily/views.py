from django.shortcuts import render
from django.http import HttpResponse
from .models import TaskList, Task

# Create your views here.
def home(request):  
    return render(request, 'index.html')

def signup(request):    
    return render(request, 'signup.html')

def daily(request, id):
    tl = TaskList.objects.get(id=id)
    return HttpResponse("<h1>%s" % tl.name)

