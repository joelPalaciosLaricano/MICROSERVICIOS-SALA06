from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import viewsets, mixins
from .models import Category
from .serializers import CategorySerializer

@method_decorator(cache_page(60), name="list")  # Caché de 60 segundos
class CategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategorySerializer