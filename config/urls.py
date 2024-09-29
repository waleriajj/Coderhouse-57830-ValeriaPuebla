# config/urls.py

from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuario/', include('usuario.urls')),
    path('', lambda request: render(request, 'home.html'), name='home'),  # Página principal
]
