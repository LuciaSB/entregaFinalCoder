from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Profile(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    image = models.ImageField(upload_to='profile_images')
    description = RichTextField()
    website = models.URLField()
    
    def __str__(self):
        return f"{self.name} {self.surname}"

class Blog(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = RichTextField()
    image = models.ImageField(upload_to='blog_images')
    posted_date = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    subject = models.CharField(max_length=100)
    body = models.TextField()
    sent_date = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    