from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.db.models import Q
from ssafy5_3.models import Student
from .models import Card, ChatMessage, Nickname
from random import randint

    # nicknames = ['꽃규정', '데스파시토', '조조교', 'MD장인', '오우마이걸', '홈카페사장', '갓덕삼', '점심시간딜러', '반장drop']
    # names = ['이규정', '한상길', '조혜인', '이다영', '권오우', '황지원', '김주현', '이민아', '조규태']

def stage1(request):
    #모든 학생들 중 해당 스테이지에서 언급되는 학생들 flag를 통해 구분하기
    students = Student.objects.all()
    nicknames = Nickname.objects.all()
    names = []
    for i in range(len(nicknames)):
        names.append(nicknames[i].student_name)

    for student in students:
        if student.name in names:
            student.flag = False       

    if request.is_ajax():
        data = serializers.serialize('json', nicknames)
        return HttpResponse(data, content_type='application/json')
    else:
        context = {
            'nicknames':nicknames,
        }
        return render(request, 'game/stage1.html', context)
    

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


@require_POST
def card_flip(request, pk):
    card = get_object_or_404(Card, pk=pk)
    cntAll = Card.objects.filter(flip__gt=0).count()

    if card.flip:
        flipped = False
        card.flip = 0
    else:
        flipped = True
        card.flip = cntAll // 2 + 1
    card.save()

    flip_cards_cnt = Card.objects.filter(Q(student_id=card.student_id) & Q(flip__gt=0)).count()

    prev_id = 0
    completed = False
    if cntAll % 2:
        if flip_cards_cnt == 2: # 짝이 잘 맞음
            prev_id = card.pk
            if cntAll == 3:
                completed = True
        else: # 짝 안맞음
            card.flip = 0
            card.save()
            tmp = Card.objects.filter(Q(flip=cntAll // 2 + 1))[0]
            prev_id = tmp.pk
            tmp.flip = 0
            tmp.save()
    
    
    flip_status = {
        'student_id': card.student_id,
        'prev_id': prev_id,
        'flipped': flipped,
        'card_url': '/media/' + str(card.card_img),
        'completed': completed
    }
    return JsonResponse(flip_status)


def stage3(request):
    return render(request, 'game/stage3.html')


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
