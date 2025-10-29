from django.urls import path
from .views import PostListView, PostDetailView

urlpatterns = [
    path('', PostListView.as_view(), name='posts-list'),
    path('<str:pk>/', PostDetailView.as_view(), name='posts-detail'),
]
