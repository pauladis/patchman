from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .form import PostForm, ReplyForm
from .models import User, Post, Reply
from django.views.generic import TemplateView
from django.views import View

class homepageView(TemplateView):

    def get(self, request):
        posts = Post.objects.all()
        user_id = request.user.id
        dict = {'posts':posts, 'user_id':user_id}
        return render(request, 'homepage.html', dict)


class new_postView(View):

    @method_decorator(login_required)
    def get(self, request):
        form = PostForm(request.POST or None, request.FILES or None)
        dict = {'form': form}
        return render(request, 'new_post.html', dict)

    @method_decorator(login_required)
    def post(self, request):
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            user = get_object_or_404(User, pk=request.user.id)
            f = form.save(commit=False)
            f.author = user
            f.author_id = user.id
            f.save()
            return redirect('homepage')
        dict = {'form':form}
        return render(request, 'new_post.html', dict)


class replyView(View):

    def get(self, request, id):
        form = ReplyForm()
        post = Post.objects.get(pk=id)
        replys = Reply.objects.filter(post_id=id)
        dict = {'form': form, 'replys': replys, 'post': post, 'user_id': request.user.id}
        return render(request, 'reply.html', dict)

    def post(self, request, id):
        form = ReplyForm(request.POST or None)
        if form.is_valid():
            post = get_object_or_404(Post, pk=id)
            f = form.save(commit=False)
            f.post = post
            f.post_id = id
            f.save()
            return redirect('reply', id=id)
        post = Post.objects.get(pk=id)
        replys = Reply.objects.filter(post_id=id)
        dict = {'form': form, 'replys': replys, 'post': post, 'user_id': request.user.id}
        return render(request, 'reply.html', dict)



class deleteView(View):

    @method_decorator(login_required)
    def get(self, request, id):
        post = get_object_or_404(Post, pk=id)
        if request.user.id == post.author_id:
            post.visible = False
            post.save()
        return redirect('homepage')



class delete_replyView(View):

    @method_decorator(login_required)
    def get(self, request, id):
        reply = get_object_or_404(Reply, pk=id)
        reply.visible = False
        reply.save()
        return redirect('homepage')



class editView(View):

    @method_decorator(login_required)
    def get(self, request, id):
        post = get_object_or_404(Post, pk=id)
        form = PostForm(request.POST or None, request.FILES or None, instance=post)
        return render(request, 'new_post.html', {'form':form})

    def post(self, request, id):
        post = get_object_or_404(Post, pk=id)
        form = PostForm(request.POST or None, request.FILES or None, instance=post)
        if form.is_valid():
            form.save()
            return redirect('homepage')
        return render(request, 'new_post.html', {'form':form})


class approveView(TemplateView):

    @method_decorator(login_required)
    def get(self, request):
        user_id = request.user.id
        posts = Post.objects.filter(author_id=user_id)
        posts_id = []
        for p in posts:
            posts_id.append(p.id)
        replys = Reply.objects.filter(approved=None, post_id__in=posts_id)
        dict = {'replys': replys}
        return render(request, 'approve.html', dict)

    @method_decorator(login_required)
    def post(self, request):
        keys = request.POST.keys()
        for k in keys:
            if k == 'csrfmiddlewaretoken':
                continue
            r = get_object_or_404(Reply, pk=int(k))
            if request.POST[k] == 'on':
                r.approved = True
            else:
                r.approved = False
            r.save()
        return redirect('homepage')
