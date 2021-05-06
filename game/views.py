from django.shortcuts import render, redirect, get_object_or_404
from ssafy5_3.models import Student
from django.http import JsonResponse
from .models import ChatMessage

def stage1(request):
    return render(request, 'game/stage1.html')


def stage2(request):
    students = Student.objects.all()
    context = {
        'students': students,
    }
    return render(request, 'game/stage2.html', context)


def stage3(request):
    pass


def bonus(request):
    return render(request, 'game/bonus.html')

def getChatMessage(request, chat_id):
    chat = get_object_or_404(ChatMessage, pk=chat_id)
    author = chat.chat_user
    context = {
        'author': author.name,
        'initial' : author.initial,
        'fg': author.fg_color,
        'bg': author.bg_color,
        'message':chat.message,
    }
    return JsonResponse(context)

def rewards(reqeust):
    pass
