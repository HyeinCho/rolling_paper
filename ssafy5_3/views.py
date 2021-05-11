from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.http import JsonResponse
from .models import Student, Professor, Greeting, Comment

def index(request):
    students = Student.objects.all()
    context = {
        'students': students,
    }
    return render(request, 'ssafy5_3/index.html', context)


def messages(request):
    pass


def collegues(request):
    students = Student.objects.all()
    juan = Professor.objects.get(pk=1)
    context = {
        'students': students,
        'juan': juan,
    }
    return render(request, 'ssafy5_3/collegues.html', context)


def greetings(request):
    greetings = get_list_or_404(Greeting)
    serialized_greetings = []
    for greeting in greetings:
        tmp = greeting.content.split('\n\n')
        greetings_content_br = []
        for s in tmp:
            greetings_content_br.extend(s.split('\n'))
            greetings_content_br.append(' ')
        greetings_content_br.pop()
        
        serialized_greetings.append({
            'id': greeting.pk,
            'content': greetings_content_br,
            'created_at': greeting.created_at,
        })
    juan = get_object_or_404(Professor, pk=1)
    context = {
        'juan': juan,
        'greetings': serialized_greetings,
    }
    return render(request, 'ssafy5_3/greetings.html', context)
