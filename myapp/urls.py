
from django.urls import path,include
from . import views

urlpatterns = [
    path('1',views.fn1,name='1'),
    path('2',views.fn2,name='2'),
    path('3',views.fn3,name='3'),
    path('a',views.assignment1,name='a'),
    path('b',views.assignment2,name='b'),
    path('c',views.assignment3,name='c'),
    path('d',views.assignment4,name='d'),
    path('e',views.form,name='e')
]