from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def fn1(request):
    return render(request,'test.html')
def fn2(request):
    return render(request,'index.html')
def fn3(request):
    return render(request,'index2.html')    
def assignment1(request):
    return render(request,'assignment1.html')
def assignment2(request):
    return render(request,'assignment2.html')    
def assignment3(request):
    return render(request,'assignment3.html')    
def assignment4(request):
     return render(request,'assignment4.html')  
def form(request):
    return render(request,'form.html')