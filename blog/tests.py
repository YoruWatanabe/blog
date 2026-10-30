
from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files.base import ContentFile
from django.test import override_settings
from .models import Product
from PIL import Image
from io import BytesIO
import tempfile


class ProductTests(TestCase):

    def image(self):
        img = Image.new('RGB', (100, 100), color='red')
        buffer = BytesIO()
        img.save(buffer, format='PNG')
        return SimpleUploadedFile(
            'test.png',
            buffer.getvalue(),
            content_type='image/png'
        )

    def test_create(self):
        r = self.client.post(
            reverse('create_product'),
            {
                'name': 'Nowy',
                'description': 'x',
                'image': self.image(),
            }
        )
        self.assertRedirects(r, reverse('product_list'))
        self.assertTrue(Product.objects.filter(name='Nowy').exists())

    def test_detail_missing_returns_404(self):
        r = self.client.get(reverse('product_detail', args=[999]))
        self.assertEqual(r.status_code, 404)
