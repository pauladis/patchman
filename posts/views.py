from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .form import PostForm, ReplyForm
from .models import User, Post, Reply


def homepage(request):
    #posts = Post.objects.filter(author_id=request.user.id)
    posts = Post.objects.all()
    replys = Reply.objects.all()
    user_id = request.user.id
    dict = {'posts':posts, 'replys':replys, 'user_id':user_id}
    return render(request, 'homepage.html', dict)

@login_required
def new_post(request):
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

def reply(request, id):
    form = ReplyForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = get_object_or_404(Post, pk=id)
        f = form.save(commit=False)
        f.post = post
        f.post_id = id
        f.save()
        return redirect('reply', id=id)
    post = Post.objects.get(pk=id)
    replys = Reply.objects.filter(post_id = id)
    dict = {'form':form, 'replys':replys, 'post':post, 'user_id':request.user.id}
    return render(request, 'reply.html', dict)

@login_required
def delete(request,id):
    post = get_object_or_404(Post, pk=id)
    if request.user.id == post.author_id:
        post.visible = False
        post.save()
    return redirect('homepage')

@login_required
def delete_reply(request,id):
    reply = get_object_or_404(Reply, pk=id)
    reply.visible = False
    reply.save()
    return redirect('homepage')

@login_required
def edit(request,id):
    post = get_object_or_404(Post, pk=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('homepage')
    return render(request, 'new_post.html', {'form':form})

@login_required
def approve(request):
    user_id = request.user.id
    posts = Post.objects.filter(author_id=user_id)
    posts_id = []
    for p in posts:
        posts_id.append(p.id)
    replys = Reply.objects.filter(approved=None, post_id__in=posts_id)
    if request.method == 'POST':
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
    dict = {'replys':replys}
    return render(request, 'approve.html', dict)