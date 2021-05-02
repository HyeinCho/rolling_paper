from django.shortcuts import render, redirect
from ssafy5_3.models import Student

def stage1(request):
    pass


def stage2(request):
    students = Student.objects.all()
    context = {
        'students': students,
    }
    return render(request, 'game/stage2.html', context)


def stage3(request):
    pass


def bonus(request):
    pass


def rewards(reqeust):
    pass
