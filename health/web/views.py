from django.shortcuts import render
from .models import Exercises

def index(request):
    return render(request, 'index.html')

def screen(request, id):
    exercise_data = Exercises.objects.get(name_en = id)
    return render(request, 'screen.html', {'exercise_data': exercise_data})

def testweb(request):
    return render(request, 'testweb.html')

def testweb2(request):
    return render(request, 'testweb2.html')

def testweb3(request):
    return render(request, 'testweb3.html')