
from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('add/', views.create_product, name='create_product'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('edit/<int:pk>/', views.edit_product, name='edit_product'),
    path('delete/<int:pk>/', views.delete_product, name='delete_product'),
    path('contact/', views.contact, name='contact'),
    path('test-error/', views.test_error, name='test_error'),
    path('contact/success/', views.contact_success, name='contact_success'),
]
