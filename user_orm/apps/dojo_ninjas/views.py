from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    response = " Hello you are in dojo ninjas"
    return HttpResponse(response)