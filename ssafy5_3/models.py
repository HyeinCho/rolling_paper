from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=10)
    nickname = models.CharField(max_length=20)
    webex_img = models.ImageField(upload_to='webex/')
    profile_img = models.ImageField(upload_to='profile/')
    name_img = models.ImageField(upload_to='name/')
    flag = models.BooleanField()
    song = models.CharField(max_length=50)
    song_url = models.CharField(max_length=100)


class Professor(models.Model):
    name = models.CharField(max_length=10)
    webex_img = models.ImageField(upload_to='webex/')
    coins = models.IntegerField()
    game_clear = models.BooleanField()
    

class Greeting(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField()


class Comment(models.Model):
    from_msg = models.ManyToManyField(Student, related_name="to_msg")
    content = models.TextField()