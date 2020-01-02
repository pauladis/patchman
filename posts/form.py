from django.forms import ModelForm
from .models import Post, Reply


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content']


class ReplyForm(ModelForm):
    class Meta:
        model = Reply
        fields = ['name','email','content']