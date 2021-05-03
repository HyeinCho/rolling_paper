from django.shortcuts import render, redirect
from ssafy5_3.models import Student
from .models import Card
from random import randint

def stage1(request):
    return render(request, 'game/stage1.html')


def stage2(request):
    if not Card.objects.all(): # 나중에 포스트로 바꿀거임
        for _ in range(4):
            while True:
                student = Student.objects.order_by("?").first()
                count_num = Card.objects.filter(student_id=student.pk).count()
                print(student.name, count_num)
                card = Card()
                card.student_id = student.pk
                card.flip = False
                
                if count_num == 2:
                    continue
                elif count_num == 1:
                    tmp = Card.objects.get(student_id=student.pk)
                    if tmp.flag: # 프로필 이미지 존재 => 이름 이미지 넣기
                        card.card_img = student.name_img
                        card.flag = False
                    else: # 이름 이미지 존재 => 프로필 이미지 넣기
                        card.card_img = student.profile_img
                        card.flag = True
                else: # count_num == 0
                    random_num = randint(0, 1)
                    if random_num: # 프로필 이미지 넣기
                        card.card_img = student.profile_img
                        card.flag = True
                    else: # random_num == 0, 이름 이미지 넣기
                        card.card_img = student.name_img
                        card.flag = False
                card.save()
                break

    cards = Card.objects.all()
    context = {
        'cards': cards,
    }
    return render(request, 'game/stage2.html', context)


def stage3(request):
    pass


def bonus(request):
    pass


def rewards(reqeust):
    pass
