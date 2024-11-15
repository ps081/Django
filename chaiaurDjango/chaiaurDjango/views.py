from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, world. You are at chain aur Django Home page")
    return render(request, 'Website/index.html')

def about(request):
    # return HttpResponse("Hello, world. You are at chain aur Django About page")
    return render(request, 'Website/about.html')

def contact(request):
    # return HttpResponse("Hello, world. You are at chain aur Django Contact page")
    return render(request, 'Website/contact.html')

def blog(request):
    # return HttpResponse("Hello, world. You are at chain aur Django Help page")
    # return render(request, 'Website/register.html')
    return render(request, 'Website/blog.html')

def shop(request):
    return render(request, 'Website/shop.html')

def sproduct(request):
    return render(request, 'Website/sproduct.html')

def cart(request):
    return render(request, 'Website/cart.html')