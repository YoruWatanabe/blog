
import csv

from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from pathlib import Path

from .models import Product
from .forms import ProductForm, ContactForm


def product_list(request):
    products = Product.objects.all()
    return render(request, 'blog/product_list.html', {
        'products': products
    })


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'blog/product_detail.html', {
        'product': product
    })


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()

    return render(request, 'blog/create.html', {'form': form})


def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = ProductForm(
            request.POST,
            request.FILES,
            instance=product
        )
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)

    return render(request, 'blog/edit.html', {
        'form': form,
        'product': product
    })


def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        product.delete()
        return redirect('product_list')

    return render(request, 'blog/delete.html', {
        'product': product
    })

def test_error(request):
    raise Exception("Test błędu 500")

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            csv_path = Path(settings.BASE_DIR) / 'responses.csv'

            with open(
                csv_path,
                'a',
                newline='',
                encoding='utf-8'
            ) as file:
                writer = csv.writer(file)
                writer.writerow([
                    data['name'],
                    data['email'],
                    data['phone'],
                    data['subject'],
                    data['message'],
                ])

            return redirect('contact_success')
    else:
        form = ContactForm()

    return render(request, 'blog/contact.html', {
        'form': form
    })


def contact_success(request):
    return render(request, 'blog/success.html')

def custom_404(request, exception):
    return redirect('https://www.youtube.com/watch?v=HcYCyj0VViI&source_ve_path=OTY3MTQ&embeds_referring_euri=https%3A%2F%2Fwww.bing.com%2F&embeds_referring_origin=https%3A%2F%2Fwww.bing.com')

def custom_500(request):
    return redirect('https://www.youtube.com/')