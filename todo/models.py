from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Todo(models.Model):
    title = models.CharField(max_length=50)
    detail = models.TextField(max_length=500)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date= models.DateTimeField(default=timezone.now)
    completed = models.BooleanField(default=False) 
    def __str__(self):
        return self.title