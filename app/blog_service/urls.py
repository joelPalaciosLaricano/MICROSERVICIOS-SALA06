from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('app.posts.urls')),
    path('api/', include('app.categories.urls')),
    path('healthz/', include('app.core.urls')),
]