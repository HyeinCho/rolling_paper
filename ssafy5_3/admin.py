from django.contrib import admin
from .models import Student, Professor, Greeting, Comment, Message

admin.site.register(Student)
admin.site.register(Professor)
admin.site.register(Greeting)
admin.site.register(Comment)
admin.site.register(Message)