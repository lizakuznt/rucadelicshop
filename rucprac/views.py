from django.http import HttpResponse
from django.shortcuts import render, redirect

from rucprac.forms import *
from rucprac.models import *


def index(request):
    return render(request,"index.html")


def catalog(request):
    product = Product.objects.all()

    return render(request, 'cataloges/catalog.html', {'products': product})


def catalog_2(request):
    return render(request, 'cataloges/catalog_2.html')


def product_about(request):
    return render(request, "actions/product_about.html", )


def feedback(request):
    return render(request, "feedback.html")

def product_add(request):
    return render(request, "actions/product_add.html", )

def product_update(request, product_id):
    return render(request, "actions/product_update.html", {'producy_id':product_id})



def shop_catalog(request):
    products = Product.objects.all()
    return render(request, 'cataloges/catalog.html', context={'products': products})

def view_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, "view_product.html", {'product': product})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalog')
    else:
        form = ProductForm()
    return render(request, "actions/product_add.html", {'form': form})


def list_tag(request):
    tags = Tag.objects.all()
    return render(request,"list_Tag", {'tags': tags})

def tag_products(request, tag_id):
    tag = Tag.objects.get(pk=tag_id)
    products = tag.Tag_FK_MTM.all()
    return render(request, "tag_output.html", {'tag': tag, 'products': products})

def array_category(request):
    categories = Category.objects.all()
    return render(request, "array_category", {'categories': categories})

def category_products(request, category_id):
    category =Category.objects.get(pk=category_id)
    products = category.product
    return render(request, "cataloges/category_products.html", {'category': category, 'products': products})

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('category_list')
    else:
        form = CategoryForm()

    return render(request, "actions/product_add.html", {'form': form})