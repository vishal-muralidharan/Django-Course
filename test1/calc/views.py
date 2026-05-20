from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html', {'name': 'Vishal'})

def add(request):
    Val1 = request.GET['num1']
    Val2 = request.GET['num2']
    Res = int(Val1) + int(Val2)

    return render(request, 'result.html', {'result': Res})