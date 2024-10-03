from django.db import models


class Post(models.Model):
    title = models.CharField(
        max_length=200, verbose_name="Blog Title"
    )  # Title of the blog post
    content = models.TextField(verbose_name="Post Content")  # Content of the blog post
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Created Date"
    )  # Date and time when the post was created
    category = models.CharField(
        max_length=100, blank=True, verbose_name="Post Category"
    )  # Category associated with the post

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog Post"  
        verbose_name_plural = "Blog Posts"  
        ordering = ["-created_at"]  # ორდერინგი შექმნის თარიღის მიხედვით დაღმავალი
