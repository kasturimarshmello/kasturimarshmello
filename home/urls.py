from django.urls import path
from .views import *

urlpatterns = [
     path('', home, name='home'),
     path('login/', login_view, name='login_view'),
     path('about/', about, name='about'),
     path('add_blog/', add_blog, name='add_blog'),
     path('my_blogs/', my_blogs, name='my_blogs'),
     path('contact/', contact, name='contact'),
     path('logout-view/', logout_view, name='logout_view'),
     path('post/<slug>', post, name='post'),
     path('delete-blog/<id>', delete_blog, name='delete_blog'),
     path('update-blog/<slug>', update_blog, name='update_blog'),
]