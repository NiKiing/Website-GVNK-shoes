from django.shortcuts import render, redirect


def indexView (request):
    return render(request, "index.html")

def productsView(request):
    return render(request, "products.html")

def contactView(request):
    return render (request, "contact.html")

def cartView(request):
    return render (request, 'cart.html')