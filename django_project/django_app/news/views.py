from django.shortcuts import render, redirect
from .models import Blog
from .forms import BlogForm


def index(request):
    data = Blog.objects.all()
    context = {
        'news' : data
    }
    return render(request, template_name='news/index.html', context=context)


def create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            news = form.save()
            return redirect(news)
    else:
        form = BlogForm()
    context = {
        'form': form
    }
    return render(request, template_name='news/create_new_post.html', context=context)