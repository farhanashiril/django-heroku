
from django.urls import path,include
from . import views

urlpatterns = [
    path('test',views.testfun,name='test'),
    path('a',views.fn1,name='a'),
    path('b',views.fn2,name='b'),
    path('c',views.assignment1,name='c'),
    path('d',views.assignment2,name='d')
]