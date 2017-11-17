from django.shortcuts import render, HttpResponse

# Create your views here.
def books(request):
    response = " Hello you are in book authors orm"
    return HttpResponse(response)