from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Student, Professor, Greeting, Comment, Message

def index(request):
    professor = Professor.objects.get(pk=1)
    context = {
        'professor': professor,
    }
    return render(request, 'ssafy5_3/index.html', context)

def messages(request):
    context = {

    }
    return render(request, 'ssafy5_3/messages.html', context)

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


# Reward 페이지의 open에 필요한 coin 개수 불러오기
def load_coin(request):
    professor = get_object_or_404(Professor, pk=1)
    coin = professor.coins
    not_opened_num = len(get_list_or_404(Message, is_locked=True))
    # DB의 coin 개수와 아직 열리지 않은 메세지 개수 중에서 더 적은 쪽을 반환한다.
    context = {
        'coin' : min(coin, not_opened_num)
    }
    return JsonResponse(context)

# DB에 있는 모든 메세지 불러오기
def load_messages(request):
    messages = get_list_or_404(Message)
    serialized_messages = []
    for message in messages:
        message_content_br = message.content.replace('\n','<br>')
        serialized_messages.append({
            'id': message.pk,
            'name': message.student.name if message.student else '<i class="fas fa-user-lock"></i>',
            'content': message_content_br,
            'isLocked' : message.is_locked,
            'textSize' : 1 if (len(message_content_br)>60) else ( 2 if (len(message_content_br)>40) else 3)
        })
    context = {
        'messages':serialized_messages,
    }
    return JsonResponse(context)

def open_message(request, id):
    # 교수님 코인 1개 감소
    professor = get_object_or_404(Professor, pk=1)
    professor.coins = professor.coins - 1
    professor.save()
    # 메세지 오픈 여부 DB 변경
    message = get_object_or_404(Message, pk=id)
    message.is_locked= False
    message.save()
    context = {
    }
    return JsonResponse(context)

# 입력한 개수 만큼의 coin을 추가한다.
@require_POST
def insert_coin(request, coin_num):
    professor = get_object_or_404(Professor, pk=1)
    professor.coins = professor.coins + coin_num
    professor.save()

    stage_num = 1 if coin_num==9 else coin_num-9
    return redirect('game:rewards', stage_num)
    
def credit(request):
    return render(request, 'ssafy5_3/credit.html')