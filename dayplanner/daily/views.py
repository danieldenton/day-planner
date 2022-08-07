from lzma import FORMAT_ALONE
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    context = {
        'name': 'Fool',
        'age': '44',
        'nationality': 'Irish'
    } 
    return render(request, 'index.html', context)

def counter(request):
    return render(request, 'counter.html')

