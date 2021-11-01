from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.files import ImageField

from random import choice
import string

# Create your models here.


class Tweet(models.Model):

    def event_code():

        a = []
        for i in range(8):
            a.append(choice(string.ascii_letters))

        return (''.join(a))

    code = models.CharField(
        default=event_code, max_length=25, primary_key=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, default=User.objects.first().pk)
    content = models.TextField(blank=False, max_length=300)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    dateTimeCreated = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.author}'s tweet"


class Like(models.Model):
    likedBy = models.ForeignKey(User, on_delete=models.CASCADE)
    tweetcode = models.CharField(max_length=25)
