from django.shortcuts import render
from .models import Post

def home(request):
    return render(request, 'blog/home.html')  # Adjust the path if necessary

def create_and_filter_posts(request):
    # Create instances of Post (you may want to do this conditionally)
    post1 = Post.objects.create(title="First Post", content="This is the content of the first post.", category="General")
    post2 = Post.objects.create(title="Second Post", content="This is the content of the second post.", category="Technology")
    post3 = Post.objects.create(title="Third Post", content="This is the content of the third post.", category="General")

    # Filter posts that belong to the "General" category
    general_posts = Post.objects.filter(category="General")

    # Render a template to display the posts
    return render(request, 'blog/posts.html', {'posts': general_posts})
