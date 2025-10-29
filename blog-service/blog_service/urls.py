from django.urls import path, include
from django.contrib import admin
from core import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # aceptar la barra final en la URL de healthcheck
    path('healthz/', core_views.healthz),
    path('api/categories/', include('categories.urls')),
    path('api/posts/', include('posts.urls')),
]
