from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("Hi I am khilesh form home route")
    return render(request, 'index.html')

def about(request):
    return HttpResponse("Hey see this is the about page of our website")

def contact(request):
    return HttpResponse("You know how to contact with me, if you dont know see here")