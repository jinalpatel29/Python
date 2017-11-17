from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    response = " Hello this is user login"
    return HttpResponse(response)