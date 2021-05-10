from django.shortcuts import render, redirect
from .models import Student, Professor, Greeting, Comment

def index(request):
    professor = Professor.objects.get(pk=1)
    context = {
        'professor': professor,
    }
    return render(request, 'ssafy5_3/index.html', context)


def messages(request):
    pass


def collegues(request):
    students = Student.objects.all()
    context = {
        'students': students,
    }
    return render(request, 'ssafy5_3/collegues.html', context)


def greetings(request):
    pass
