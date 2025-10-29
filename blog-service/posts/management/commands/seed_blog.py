from django.core.management.base import BaseCommand
from categories.models import Category
from authors.models import Author
from posts.models import Post
from slugify import slugify
import random

class Command(BaseCommand):
    help = 'Seed the blog with sample categories, authors and posts'

    def handle(self, *args, **options):
        self.stdout.write('Seeding categories...')
        categories = []
        for i in range(1,6):
            c, _ = Category.objects.get_or_create(name=f'Category {i}', slug=slugify(f'Category {i}'))
            categories.append(c)

        self.stdout.write('Seeding authors...')
        authors = []
        for i in range(1,4):
            a, _ = Author.objects.get_or_create(display_name=f'Author {i}', email=f'author{i}@example.com')
            authors.append(a)

        self.stdout.write('Seeding posts...')
        for i in range(1,31):
            title = f'Post number {i}'
            body = f'This is the body of post {i}. ' * 10
            author = random.choice(authors)
            category = random.choice(categories)
            status = 'published' if random.random() > 0.2 else 'draft'
            Post.objects.create(title=title, body=body, author=author, category=category, status=status)

        self.stdout.write(self.style.SUCCESS('Seeding complete'))
