from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})


    def __str__(self):
        return self.title

class Comment(models.Model):
    content=models.CharField(max_length=500,blank=True,null=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    date_posted=models.DateTimeField(default=timezone.now,null=True)



    def get_absolute_url(self):
        return reverse('blog-home')


 

