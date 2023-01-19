from django.urls import path
from .views import *

urlpatterns = [
     path('', home, name='home'),
     path('login/', login_view, name='login_view'),
     path('about/', about, name='about'),
     path('contact/', contact, name='contact'),
     path('post/', post, name='post'),
]