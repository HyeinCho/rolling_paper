from django.db import models

class Card(models.Model):
    student_id = models.IntegerField()
    card_img = models.ImageField()
    flag = models.BooleanField()
    flip = models.IntegerField()

    def __str__(self):
        return f'{self.pk} - {self.student_id} - {self.flip}'

# Bonus - 유튜브 채팅용 데이터 모델들
class ChatUser(models.Model):
    name = models.CharField(max_length=10)
    initial = models.CharField(max_length=2)
    fg_color = models.CharField(max_length=8)
    bg_color = models.CharField(max_length=8)

    def __str__(self):
        return self.name
    
class ChatMessage(models.Model):
    chat_user = models.ForeignKey(ChatUser, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return self.chat_user.name +"|"+ self.message
    

class BalanceGame(models.Model):
    title = models.CharField(max_length=30)
    question1 = models.CharField(max_length=50)
    question2 = models.CharField(max_length=50)
    # 나중에 확장할 때, 계정이랑 외래키 연결하기
    vote1 = models.IntegerField()
    vote2 = models.IntegerField()

    def __str__(self):
        return f'{self.title} - {self.question1} - {self.question2}'

