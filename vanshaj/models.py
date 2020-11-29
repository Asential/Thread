from django.contrib.auth.models import AbstractUser
from django.db import models
from django import forms
from datetime import datetime
import uuid 

class User(AbstractUser):
    pass

class Topic(models.Model):
    topic = models.CharField(max_length=150)
    url = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.topic}"


class Comment(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField(max_length=500)
    allowed = models.BooleanField(default=True)
    createdTime = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='replies')
    
    def __str__(self):
        return f"{self.user}: {self.content}"
    
class CommentForm(forms.ModelForm):  
    class Meta:  
        model = Comment
        fields = ['content']