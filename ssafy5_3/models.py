from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=10)
    nickname = models.CharField(max_length=20)
    webex_img = models.ImageField(upload_to='webex/')
    profile_img = models.ImageField(upload_to='profile/')
    name_img = models.ImageField(upload_to='name/')
    card_img = models.ImageField(upload_to='card/')
    flag = models.BooleanField()
    song = models.CharField(max_length=50)
    song_url = models.CharField(max_length=100)
    git_url = models.CharField(max_length=100, blank=True)
    insta_url = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.name
    

    def __str__(self):
        return f'{self.pk} - {self.name}'
    


class Professor(models.Model):
    name = models.CharField(max_length=10)
    webex_img = models.ImageField(upload_to='webex/')
    coins = models.IntegerField()
    game_clear = models.BooleanField()

    def __str__(self):
        return f'{self.pk} - {self.name}'
    

class Greeting(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField()


class Comment(models.Model):
    from_msg = models.ManyToManyField(Student, related_name="to_msg")
    content = models.TextField()


class Message(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    is_locked = models.BooleanField(default=True)

    def __str__(self):
        if self.student:
            return f'{self.student.name} - {self.content}'
        else:
            return f'{self.content}'