from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    text = {
        "name": "Sages",
        "number": 20
    }
    return render(request, 'index.html', context=text)