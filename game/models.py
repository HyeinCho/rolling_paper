from django.db import models

class Card(models.Model):
    student_id = models.IntegerField()
    card_img = models.ImageField()
    flag = models.BooleanField()
    flip = models.BooleanField()