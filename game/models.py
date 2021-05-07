from django.db import models

class Card(models.Model):
    student_id = models.IntegerField()
    card_img = models.ImageField()
    flag = models.BooleanField()
    flip = models.IntegerField()

    def __str__(self):
        return f'{self.pk} - {self.student_id} - {self.flip}'