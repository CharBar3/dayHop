from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    date = models.DateField('post date')
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=280)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.date}'

    def get_absolute_url(self):
        return reverse('posts_detail', kwargs={'post_id': self.id})
