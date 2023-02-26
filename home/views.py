from django.shortcuts import render, redirect
from .models import *
from .form import *
from django.http import HttpResponse
from django.contrib.auth import logout

# Create your views here.
def logout_view(request):
    logout(request)
    return redirect('/')

def home(request):
    context = {'blogs' : BlogModel.objects.all()}
    return render(request, 'home.html', context)

def login_view(request):
    return render(request, 'login.html')

def about(request):
    return render(request, 'about.html')

def add_blog(request):
    context = {
        'form' : BlogForm
    }
    try:
        if request.method == 'POST':
            form = BlogForm(request.POST, request.FILES)
            title = request.POST.get('title')
            user = request.user
            if form.is_valid():
                content = form.cleaned_data['content']
                image = form.cleaned_data['image']

            blog_model = BlogModel.objects.create(
                user = user, title = title,
                content = content,  image = image
                )
            print(blog_model)
            return redirect('/add_blog/')

    except Exception as e:
        print(e)

    return render(request, 'add_blog.html', context)

def contact(request):
    return render(request, 'contact.html')

def my_blogs(request):
    context = {}
    try:
        blog_list = BlogModel.objects.filter(user = request.user)
        context['blogs'] = blog_list
        context['user'] = request.user
    except Exception as e:
        print(e)
    return render(request, 'my_blogs.html', context)

def delete_blog(request, id):
    context = {}
    try:
        blog_obj = BlogModel.objects.get(id = id)
        
        if blog_obj.user == request.user:
            blog_obj.delete()
    except Exception as e:
        print(e)
    return redirect('/my_blogs/')

def update_blog(request, slug):
    context = {}
    try:
        blog_obj = BlogModel.objects.get(slug = slug)
        initial_dict = {'content' : blog_obj.content}
        form = BlogForm(initial = initial_dict)
        if blog_obj.user != request.user:
            return redirect('/')
        context['blog_obj'] = blog_obj
        context['form'] = form
        if request.method == 'POST':
            form = BlogForm(request.POST, request.FILES)
            title = request.POST.get('title')
            user = request.user
            if form.is_valid():
                content = form.cleaned_data['content']
                image = form.cleaned_data['image']

            # blog_model = BlogModel.objects.get(slug = slug)
            print("This>>>> ", blog_obj)
            blog_obj.title = title
            blog_obj.content = content
            blog_obj.image = image
            blog_obj.save()
    except Exception as e:
        print(e)
    return render(request, 'update_blog.html', context)

def post(request, slug):
    context = {}
    try:
        blog_obj = BlogModel.objects.filter(slug = slug).first()
        context['blog'] = blog_obj
    except Exception as e:
        print(e)
    return render(request, 'post.html', context)





# def detail(request, slug):
#     q = BlogModel.objects.filter(slug__iexact = slug)
#     if q.exists():
#        q = q.first()
#     else:
#        return HttpResponse('<h1>Post Not Found</h1>')
#     context = {
 
#        'post': q
#     }
#     return render(request, 'posts/details.html', context)