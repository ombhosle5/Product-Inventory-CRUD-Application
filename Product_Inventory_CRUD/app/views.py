from django.shortcuts import render  , redirect ,get_object_or_404
from .models import Product
from .forms import ProductForm
# Create your views here.

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product/product.html' , {'products':products})

def product_view(request):
    products = Product.objects.all()
    return render(request, 'product/home_product.html' , {'products':products})

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST,  request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()

    return render(request , 'product/product_form.html', {'form':form})


def update_product(request, pk):
    product = get_object_or_404(Product , pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES ,instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product/product_form.html', {'form':form})

def delete_product(request, pk):
    product = get_object_or_404(Product , pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return redirect('product_list')
