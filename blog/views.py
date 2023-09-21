from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Blog
from .forms import BlogForm

def all_blogs(request):
    blogs = Blog.objects.all()

    context = {
        'blogs':blogs
    }
    return render(request, 'bloglar.html',context)

def blog_detail(request, pk):
    blog = Blog.objects.get(id=pk)

    context = {
        'blog':blog
    }
    return render(request, 'blog.html', context)

def create_blog(request):
    form = BlogForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponse("Ma'lumot bazaga saqlandi!")
    
    context = {
        'form':form
    }
    return render(request, 'create-blog.html',context)

def update_blog(request, pk):

    blog = Blog.objects.get(id=pk)

    form = BlogForm(request.POST or None, instance=blog)
    if form.is_valid():
        form.save()
        return HttpResponse("Ma'lumot o'zgartirildi!")
    

    context = {
        'form':form
    }

    return render(request, 'update_blog.html', context)

def delete_blog(request, pk):
    blog = Blog.objects.get(id=pk)
    blog.delete()
    return redirect('all_blogs')