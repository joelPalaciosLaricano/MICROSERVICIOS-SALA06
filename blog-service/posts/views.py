from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework import generics
from django.db.models import Q
from .models import Post
from .serializers import PostListSerializer, PostDetailSerializer


class PostListView(generics.ListAPIView):
    serializer_class = PostListSerializer

    def get_queryset(self):
        qs = Post.objects.filter(status='published').select_related('author', 'category')
        search = self.request.query_params.get('search')
        if search:
            qs = qs.filter(Q(title__icontains=search) | Q(body__icontains=search))
        return qs.order_by('-published_at')


@method_decorator(cache_page(90), name='get')
class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.select_related('author', 'category')
    serializer_class = PostDetailSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        # default retrieve behavior; increment views when served
        response = super().get(request, *args, **kwargs)
        try:
            obj = self.get_object()
            obj.views = (obj.views or 0) + 1
            obj.save(update_fields=['views'])
        except Exception:
            pass
        return response
from django.db.models import Q
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import Post
from .serializers import PostListSerializer, PostDetailSerializer

class PostListView(generics.ListAPIView):
    serializer_class = PostListSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        qs = Post.objects.filter(status='published').select_related('author', 'category').order_by('-published_at')
        q = self.request.GET.get('search')
        if q:
            qs = qs.filter(Q(title__icontains=q) | Q(body__icontains=q))
        return qs


@method_decorator(cache_page(60), name='dispatch')
class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.filter(status='published').select_related('author', 'category')
    serializer_class = PostDetailSerializer

    def get_object(self):
        lookup = self.kwargs.get('pk')
        # allow numeric pk or slug
        obj = None
        try:
            if lookup.isdigit():
                obj = self.queryset.get(pk=int(lookup))
        except Exception:
            obj = None
        if obj is None:
            obj = generics.get_object_or_404(self.queryset, slug=lookup)
        # increment views (fire-and-forget)
        try:
            Post.objects.filter(pk=obj.pk).update(views=obj.views + 1)
        except Exception:
            pass
        return obj
