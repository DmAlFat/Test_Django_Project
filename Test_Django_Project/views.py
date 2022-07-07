from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return HttpResponse("This is my first test django project what is reversing your inputed text.")

def home(request):
    return render(request, 'home.html')