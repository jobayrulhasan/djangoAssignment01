from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def staticFile (request):
    return render(request, 'static/index.html')
