from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.db.models import Q
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from .models import Post
from .serializers import PostListSerializer, PostDetailSerializer

@method_decorator(cache_page(60), name="retrieve")  # Caché de 60 segundos para el detalle
class PostViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Post.objects.filter(status="published").select_related("author", "category")
    lookup_field = 'slug'
    
    def get_serializer_class(self):
        return PostDetailSerializer if self.action == "retrieve" else PostListSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get('search', None)
        
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) | Q(body__icontains=search_query)
            )
        
        return queryset
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # Incrementar contador de vistas
        instance.views += 1
        instance.save(update_fields=['views'])
        
        serializer = self.get_serializer(instance)
        return Response(serializer.data)