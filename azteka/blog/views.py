from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Category
# Create your views here.


class BlogView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'post_list'
    paginate_by = 5


class CategoryView(DetailView):
    model = Category
    template_name = 'blog/category.html'