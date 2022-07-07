from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return HttpResponse("This is my first test django project what is reversing your inputed text.")

def home(request):
    return render(request, 'home.html')

def result(request):
    user_text = request.GET['usertext']
    words = user_text.split()
    number_of_words = len(words)
    reversed_text = request.GET['usertext'][::-1]
    return render(request, 'result.html', {'usertext': user_text, 'reversedtext': reversed_text, 'number_of_words': number_of_words})