from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.PROTECT, editable=False)
    date = models.DateTimeField(default=now, editable=False)
    visible = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='post_photo', null=True, blank=True)

    def __str__(self):
        return self.title

class Reply(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.PROTECT)
    date = models.DateTimeField(default=now, editable=False)
    visible = models.BooleanField(default=True)
    approved = models.NullBooleanField(default=None)

    def __str__(self):
        return self.content