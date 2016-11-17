from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')

def about(request):
    dumb = None
    if request.method == 'GET':
        dumb = "this was a GET"
    elif request.method == 'POST':
        dumb = request.POST['dumb']
    return render(request,'about.html',{'dumb':dumb})

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})
