from django.shortcuts import render, redirect
from ssafy5_3.models import Student

def stage1(request):
    students = Student.objects.all()
    # nicknames = {
    #     '이규정': '꽃규정',
    #     '한상길': '데스파시토',
    #     '조혜인': '조조교',
    #     '이다영': 'MD장인',
    #     '권오우': '오우마이걸',
    #     '황지원': '갓덕삼',
    #     '김주현': '반장drop',
    #     ''
    # }
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
    pass


def rewards(reqeust):
    pass
