from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def showTag (request):
    return render(request, 'temTag/temTag.html', {'TagValue':33}) # this dictionary is for only one pair

def ShowTagforMultiple (request):
    value1 = 'This is for value one'
    value2 = 'This is for value two'
    value3 = 'This is for value three' 
    value4 = 'This is for value four'
    
    makeDictionary = {
        'v1': value1,
        'v2': value2,
        'v3': value3,
        'v4': value4
    }
    return render(request, 'temTag/temTag.html', makeDictionary) # this dictionary is for multiple pairs