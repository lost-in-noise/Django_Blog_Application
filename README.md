# Django Blog Application

This project is a simple blog application built using Django. It allows you to create and filter blog posts by category, and manage them through the Django admin interface.

## Features
- Create blog posts with a title, content, and category.
- Filter blog posts by category.
- Manage blog posts through the Django admin interface.

## Prerequisites
Before starting, make sure you have the following installed:
- [Python 3.12+](https://www.python.org/downloads/)
- [Django 5.1+](https://docs.djangoproject.com/en/stable/)

## Getting Started

### 1. Initialize a Django Project
- Create a virtual environment:
    ```bash
    python -m venv env
    ```
- Activate the virtual environment:
    - For Windows:
        ```bash
        .\env\Scripts\activate
        ```
    - For MacOS/Linux:
        ```bash
        source env/bin/activate
        ```
- Install Django in the virtual environment:
    ```bash
    pip install django
    ```

### 2. Set Up a New Django Project
- Start a new Django project:
    ```bash
    django-admin startproject blog_project
    ```
- Change to the project directory:
    ```bash
    cd blog_project
    ```

### 3. Create a Django Application
- Create a new app called `blog`:
    ```bash
    python manage.py startapp blog
    ```

### 4. Define Models
- In `blog/models.py`, add the following model to create a `Post` model:
    ```python
    from django.db import models

    class Post(models.Model):
        title = models.CharField(max_length=255)
        content = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)
        category = models.CharField(max_length=100)

        def __str__(self):
            return self.title
    ```

### 5. Run Migrations
- Make and apply migrations to update the database:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

### 6. Create Superuser
- Create a Django superuser for managing the blog posts in the admin panel:
    ```bash
    python manage.py createsuperuser
    ```
  - Follow the prompts to create the superuser.

### 7. Running the Development Server
- Start the Django development server:
    ```bash
    python manage.py runserver
    ```
- The server will run at `http://127.0.0.1:8000/`.

### 8. Creating and Filtering Posts
- In `blog/views.py`, define a view to create and filter blog posts by category:
    ```python
    from django.shortcuts import render
    from .models import Post

    def create_and_filter_posts(request):
        # Create instances of Post
        post1 = Post.objects.create(title="First Post", content="This is the content of the first post.", category="General")
        post2 = Post.objects.create(title="Second Post", content="This is the content of the second post.", category="Technology")
        post3 = Post.objects.create(title="Third Post", content="This is the content of the third post.", category="General")

        # Filter posts by category
        general_posts = Post.objects.filter(category="General")

        # Render posts to a template
        return render(request, 'blog/posts.html', {'posts': general_posts})
    ```

### 9. Accessing the Admin Panel
- To manage blog posts through the admin interface, go to:
    ```
    http://127.0.0.1:8000/admin/
    ```

## License
This project is licensed under the MIT License.

