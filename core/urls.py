from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

handler404 = 'blog.views.custom_404'
handler500 = 'blog.views.custom_500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),   # resztę adresów obsługuje aplikacja blog
]

#if settings.DEBUG:  # w trybie deweloperskim serwujemy wgrane obrazki
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

