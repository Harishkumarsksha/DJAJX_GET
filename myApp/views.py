from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Post, Like


def home(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'myApp/base.html', context)


def like(request):
    if request.method == 'GET':
        post_id = request.GET['post_id']
        likedpost = Post.objects.get(id=post_id)
        m = Like(post=likedpost)
        m.save()
        return HttpResponse('success')
    else:
        return HttpResponse("unsuccesful")
