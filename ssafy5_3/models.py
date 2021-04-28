from django.db import models

class Students(models.Model):
    name = models.CharField(max_length=10)
    message = models.TextField()
    webex_img = models.ImageField()
    profile_img = models.ImageField()


class Professor(models.Model):
    name = models.CharField(max_length=10)
    webex_img = models.ImageField()
    

class Greetings(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    content = models.TextField()
