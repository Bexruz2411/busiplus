from django.urls import path
from .views import *

urlpatterns =[
    path('', main, name='main'),
    path('blog', blog, name='blog'),
    path('contact', contact, name='contact'),
    path('services', services, name='services'),
]