from django.db import models
from ckeditor.fields import RichTextField

class User(models.Model):
    username = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    password = models.CharField(max_length=100)

class Profile(User):
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    image = models.ImageField(upload_to='profile_images')
    description = models.TextField()
    website = models.URLField()

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()
    image = models.ImageField(upload_to='blog_images')
    posted_date = models.DateTimeField(auto_now_add=True)
    