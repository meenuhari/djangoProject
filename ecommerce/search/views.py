from django.db.models import Q
from django.shortcuts import render

from shop.models import Product


# Create your views here.
def search(request):
    query=""
    products=None
    if(request.method=="POST"):
        query=request.POST['q']
        if(query):
            products=Product.objects.filter(Q(name__icontains=query) | Q(desc__icontains=query))
    return render(request, template_name="search.html",context={'query':query,'p':products})
