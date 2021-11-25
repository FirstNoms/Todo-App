import datetime

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from To_Do.forms import TodoForm


def index(request):
    text = {
        "name": "Sages",
        "number": 20,
        "date": datetime.datetime.utcnow
    }
    return render(request, 'index.html', context=text)

def forms_display(request):
    forms = TodoForm
    if (request.method == 'POST'):
        forms= TodoForm(request.POST)

        if forms.is_valid:
            forms.save()
            return HttpResponse("Thanks for registering")
    return render(request, 'forms.html', context={"forms":forms})
