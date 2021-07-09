from django.shortcuts import render

# Create your views here.


def show_home_page(request,*args, **kwargs):
    context={}
    return render(request,'home_page/home_page.html',context)

def show_about_page(request,*args, **kwargs):
    context={}
    return render(request,'about_page/about_page.html',context)