from django.db import models
from django.utils.text import slugify
from app.authors.models import Author
from app.categories.models import Category

class Post(models.Model):
    STATUS_CHOICES = (
        ('published', 'Published'),
        ('draft', 'Draft'),
    )
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    body = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    published_at = models.DateTimeField(null=True, blank=True)
    views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-published_at']
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)