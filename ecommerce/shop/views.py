from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

from shop.models import Category

from shop.models import Product


# Create your views here.
def allcategory(request):
    p=Category.objects.all()
    return render(request,template_name="category.html",context={'p':p})
def allproducts(request,p):
    c=Category.objects.get(name=p)
    p=Product.objects.filter(category=c)
    return render(request,template_name="product.html",context={'c':c,'p':p})
def details(request,p):

    p = Product.objects.get(name=p)
    return render(request, template_name="detail.html", context={'p': p})
def register(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        cp=request.POST['cp']
        fname=request.POST['f']
        lname=request.POST['l']
        e=request.POST['e']
        if(p==cp):
            u=User.objects.create_user(username=u,password=p,first_name=fname,last_name=lname,email=e)
            u.save()
            return userlogin(request)
        else:
            return HttpResponse("passwords are not same")
    return render(request,template_name="register.html")
def userlogin(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return allcategory(request)
        else:
            return HttpResponse("Invalid credentials")

    return render(request, template_name="login.html")
@login_required
def userlogout(request):
   logout(request)
   return userlogin(request)

