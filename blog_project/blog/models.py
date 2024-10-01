from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)  # Title of the blog post
    content = models.TextField()  # Content of the blog post
    created_at = models.DateTimeField(default=timezone.now)  # Date and time when the post was created
    category = models.CharField(max_length=100, blank=True)  # Category associated with the post

    def __str__(self):
        return self.title