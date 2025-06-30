from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def showTag (request):
    return render(request, 'temTag/temTag.html')