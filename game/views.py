from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.views.decorators.http import require_POST, require_http_methods
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from ssafy5_3.models import Student
from .models import Card, ChatMessage, BalanceGame, Nickname
from ssafy5_3.models import Message, Professor
from random import randint, random

@login_required
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
    # if not Card.objects.all(): # 나중에 포스트로 바꿀거임
    if request.method == 'POST':
        Card.objects.all().delete()

        for _ in range(20):
            while True:
                student = Student.objects.order_by("?").first()
                count_num = Card.objects.filter(student_id=student.pk).count()
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
                    else: # 이름 이미지 존재 => 카드 이미지 넣기
                        card.card_img = student.card_img
                        card.flag = True
                else: # count_num == 0
                    random_num = randint(0, 1)
                    if random_num: # 프로필 이미지 넣기
                        card.card_img = student.card_img
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

    current_progress = cntAll / 20 * 100
    prev_id = 0
    completed = False
    if cntAll % 2:
        if flip_cards_cnt == 2: # 짝이 잘 맞음
            prev_id = card.pk
            current_progress = (cntAll + 1) / 20 * 100
            if cntAll == 19:
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
        'completed': completed,
        'current_progress': current_progress,
    }
    return JsonResponse(flip_status)


@require_POST
def balance_game(request, pk):
    game = get_object_or_404(BalanceGame, pk=pk)

    context = {
        'title': game.title,
        'question1': game.question1,
        'question2': game.question2,
    }
    return JsonResponse(context)

@require_POST
def choose_one(request, game_pk, choice_pk):
    game = get_object_or_404(BalanceGame, pk=game_pk)

    if choice_pk == 1:
        game.vote1 += 1
    else:
        game.vote2 += 1
    game.save()

    data = {}
    return JsonResponse(data)


@require_http_methods(['GET', 'POST'])
def getHint(request, pk):
    if request.method == 'GET':
        return JsonResponse({})
    elif request.method == 'POST':
        card = get_object_or_404(Card, pk=pk)
        data = {
            'flipped': card.flip,
            'card_url': '/media/' + str(card.card_img),
        }
        return JsonResponse(data)


@require_POST
def endGame2(request):
    # students = Student.objects.all()
    cards = Card.objects.all()
    for card in cards:
        student = Student.objects.get(pk=card.student_id)
        student.flag = True
        student.save()
    
    return redirect(bonus)

def stage3(request):
    attended_students = sorted(Student.objects.filter(flag=True), key=lambda x: random())
    row1 = attended_students[:4]
    row2 = attended_students[4:9]
    row3 = attended_students[9:14]
    row4 = attended_students[14:19]
    row5 = attended_students[19]
    context = {
        'attended_students': attended_students,
        'row1': row1,
        'row2': row2,
        'row3': row3,
        'row4': row4,
        'row5': row5,
    }    
    return render(request, 'game/stage3.html', context)

def is_absent(request):
    absent_students = get_list_or_404(Student)
    if request.method == 'GET':
        serialized_students = []
        for student in absent_students:
            if student.flag == False:
                student_name = student.name[1:]
                serialized_students.append({
                    'id': student.pk,
                    'name': student_name,
                    'webex_img': str(student.webex_img),
                    'flag': student.flag,
                })
        context = {
            'absents': serialized_students,
        }
        return JsonResponse(context)
    elif request.method == 'POST':
        attended_id = request.nowAttendedId
        for attended in attended_id:
            absent_student = get_object_or_404(Student)
            absent_student.flag = True
            

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

def rewards(request):
    messages = get_list_or_404(Message)
    context = {
        'messages' : messages,
    }
    return render(request, 'game/rewards.html', context)