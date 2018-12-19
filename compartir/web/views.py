from django.http import HttpResponse
from django.shortcuts import render

from .models import Product, Category, New


def index(request):
    categorys = Category.objects.all()
    context =  {
        'categorys':categorys,
    }
    return render(request,'web/index.html',context)


def productsnew(request, id=None):
    if id is None:
        products = Product.objects.all()
        category = None
    else:
        category = Category.objects.get (id=id)
        products = Product.objects.filter(category=id)
    context =  {
        'products': products,
        'category': category,
    }
    return render (request, "web/productsnew.html", context)


def news(request):
        news = New.objects.all()
        context =  {
            'news':news,
        }
        return render (request,"web/news.html",context)


def conditions(request):
    return render (request,"web/conditions.html")


def new(request,title = None, code= None):
    new = New.objects.get (id=code)
    context =  {
        'noticia':new,
    }
    return render (request,"web/new.html",context)


def category(request, title, code):
    category = Category.objects.get (id=code)
    context =  {
        'categoria':category,
    }
    return render (request,"web/category.html",context)

def product(request, title, code):
    product = Product.objects.get(id=code)
    context =  {
        'product':product,
    }
    return render (request,"web/product.html",context)
