# Django Blog Application

This is a simple blog application built with Django. It allows users to view and filter blog posts by category, with post management available via the Django admin panel.

## Features
- Home page displaying a list of blog posts.
- Filter blog posts by category.
- Display up to 10 blog posts per page.
- Manage blog posts through the Django admin panel (add, edit, delete).
- Create, view, and filter blog posts.

## Prerequisites
Before starting, make sure you have the following installed:
- [Python 3.12+](https://www.python.org/downloads/)
- [Django 5.1+](https://docs.djangoproject.com/en/stable/)


###  Accessing the Admin Panel
- To manage blog posts through the admin interface, go to:
    ```
    http://127.0.0.1:8000/admin/
    ```

### Usage
#### Adding Posts
You can add posts using the Django admin panel. Once logged in as the superuser, you can:

1. Add new posts with a title, content, and category.
2. Edit or delete existing posts.
####  Filtering Posts
On the home page, users can filter blog posts by category using the dropdown filter.

### Future Enhancements
- Implement pagination for blog posts.
- Add user authentication to allow users to create and comment on posts.
- Enhance post filtering by adding more categories and search functionality.
