from django.shortcuts import render, redirect
from post.models import Post
# Create your views here.




def create_post(request):
    '''发表帖子，视图处理'''
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        post = Post.objects.create(title=title,content=content)
        return redirect('/post/read/?post_id=%d' % post.id)
    else:
        return render(request,'create_post.html')


def edit_post(request):
    '''帖子修改'''

    if request.method == 'POST':
        post_id = int(request.POST.get('post_id'))
        post = Post.objects.get(pk=post_id)

        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('/post/read/?post_id=%d' % post.id)
    else:
        post_id = int(request.GET.get('post_id'))
        post =  Post.objects.get(pk=post_id)
        return render(request,'edit_post.html',{"post":post})


def read_post(request):
    '''帖子的阅读页面'''

    post_id = int(request.GET.get('post_id'))
    post = Post.objects.get(pk=post_id)
    return render(request,'read_post.html',{'post':post})


def delete_post(request):
    '''帖子的删除'''
    post_id = int(request.GET.get('post_id'))
    Post.objects.get(pk=post_id).delete()
    return redirect('/')


def post_list(request):
    '''帖子的展示'''
    post = Post.objects.all()
    return render(request, 'post_list.html', {'posts': post})


def search(request):
    '''帖子的查找'''

    keyword = request.POST.get('keyword')
    posts = Post.objects.filter(content__contains=keyword)
    return render(request,'search.html',{'posts':posts})










