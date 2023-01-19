from django.shortcuts import render
from .models import *
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def login_view(request):
    return render(request, 'login.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def post(request):
    return render(request, 'post.html')





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