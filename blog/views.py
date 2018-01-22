from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse('homepage')
    return render(request,'home.html')

def bio(request):
    #return HttpResponse ('bio')
    return render(request, 'bio.html')

