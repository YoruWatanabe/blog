from django import forms
from .models import Product
from django.shortcuts import redirect


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image']


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Imię')
    email = forms.EmailField(label='E-mail')
    phone = forms.CharField(
        max_length=15,
        required=False,
        label='Telefon'
    )
    subject = forms.CharField(max_length=100, label='Temat')
    message = forms.CharField(
        widget=forms.Textarea,
        label='Wiadomość'
    )
def custom_404(request, exception):
    return redirect('product_list')
