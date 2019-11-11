from django.db import models
from django.utils import timezone


class Post(models.Model):
    is_boast = models.BooleanField(default=True)
    content = models.CharField(max_length=280)
    author = models.CharField(max_length=20)
    up_votes = models.IntegerField(default=0)
    down_vote = models.IntegerField(default=0)
    post_date = models.DateTimeField(default=timezone.now)
    net_votes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.content} - {self.author}"
