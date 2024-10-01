from django.shortcuts import render
from .models import Post

def home(request):
    category = request.GET.get('category')
    if category:
        posts = Post.objects.filter(category=category)[:10]
    else:
        posts = Post.objects.all()[:10]
    return render(request, 'blog/home.html', {'posts': posts})

