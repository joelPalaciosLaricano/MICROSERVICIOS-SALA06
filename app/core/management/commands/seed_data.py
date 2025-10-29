import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from django.utils import timezone
from app.categories.models import Category
from app.authors.models import Author
from app.posts.models import Post

class Command(BaseCommand):
    help = 'Seed the database with sample data'

    def add_arguments(self, parser):
        parser.add_argument(
            '--categories',
            default=5,
            type=int,
            help='Number of categories to create'
        )
        parser.add_argument(
            '--authors',
            default=10,
            type=int,
            help='Number of authors to create'
        )
        parser.add_argument(
            '--posts',
            default=50,
            type=int,
            help='Number of posts to create'
        )

    def handle(self, *args, **options):
        num_categories = options['categories']
        num_authors = options['authors']
        num_posts = options['posts']
        
        self.stdout.write(self.style.SUCCESS(f'Creating {num_categories} categories...'))
        categories = self._create_categories(num_categories)
        
        self.stdout.write(self.style.SUCCESS(f'Creating {num_authors} authors...'))
        authors = self._create_authors(num_authors)
        
        self.stdout.write(self.style.SUCCESS(f'Creating {num_posts} posts...'))
        self._create_posts(num_posts, authors, categories)
        
        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))

    def _create_categories(self, count):
        categories = []
        category_names = [
            'Tecnología', 'Ciencia', 'Deportes', 'Cultura', 'Política',
            'Economía', 'Salud', 'Educación', 'Entretenimiento', 'Viajes'
        ]
        
        # Asegurarse de no exceder la cantidad de nombres disponibles
        count = min(count, len(category_names))
        
        for i in range(count):
            category, created = Category.objects.get_or_create(
                name=category_names[i],
                defaults={'is_active': True}
            )
            categories.append(category)
            if created:
                self.stdout.write(f'  - Created category: {category.name}')
            else:
                self.stdout.write(f'  - Category already exists: {category.name}')
        
        return categories

    def _create_authors(self, count):
        authors = []
        domains = ['gmail.com', 'hotmail.com', 'yahoo.com', 'outlook.com']
        
        for i in range(count):
            first_name = random.choice(['Juan', 'María', 'Pedro', 'Ana', 'Luis', 'Sofía', 'Carlos', 'Laura', 'Miguel', 'Elena'])
            last_name = random.choice(['García', 'Rodríguez', 'López', 'Martínez', 'González', 'Pérez', 'Sánchez', 'Romero', 'Torres', 'Díaz'])
            display_name = f"{first_name} {last_name}"
            email = f"{first_name.lower()}.{last_name.lower()}@{random.choice(domains)}"
            
            author, created = Author.objects.get_or_create(
                email=email,
                defaults={'display_name': display_name}
            )
            authors.append(author)
            if created:
                self.stdout.write(f'  - Created author: {author.display_name} ({author.email})')
            else:
                self.stdout.write(f'  - Author already exists: {author.display_name} ({author.email})')
        
        return authors

    def _create_posts(self, count, authors, categories):
        if not authors or not categories:
            self.stdout.write(self.style.ERROR('Cannot create posts: No authors or categories available'))
            return
        
        titles = [
            'Cómo mejorar tu productividad', 
            'Los mejores destinos para viajar', 
            'Tendencias tecnológicas para este año',
            'Consejos para una alimentación saludable',
            'El impacto de la inteligencia artificial',
            'Cómo invertir en bolsa para principiantes',
            'Los beneficios del ejercicio diario',
            'Novedades en el mundo del cine',
            'Claves para aprender un nuevo idioma',
            'El futuro de las energías renovables'
        ]
        
        paragraphs = [
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam auctor, nisl eget ultricies tincidunt, nisl nisl aliquam nisl, eget aliquam nisl nisl eget nisl.',
            'Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante.',
            'Donec eu libero sit amet quam egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend leo. Quisque sit amet est et sapien ullamcorper pharetra.',
            'Vestibulum erat wisi, condimentum sed, commodo vitae, ornare sit amet, wisi. Aenean fermentum, elit eget tincidunt condimentum, eros ipsum rutrum orci, sagittis tempus lacus enim ac dui.',
            'Donec non enim in turpis pulvinar facilisis. Ut felis. Praesent dapibus, neque id cursus faucibus, tortor neque egestas augue, eu vulputate magna eros eu erat.'
        ]
        
        for i in range(count):
            title = f"{random.choice(titles)} {i+1}"
            body = '\n\n'.join(random.sample(paragraphs, k=min(len(paragraphs), random.randint(2, 5))))
            
            # Fecha de publicación aleatoria en los últimos 30 días
            days_ago = random.randint(0, 30)
            published_at = timezone.now() - timedelta(days=days_ago)
            
            # Estado aleatorio con mayor probabilidad de publicado
            status = random.choices(['draft', 'published'], weights=[0.2, 0.8])[0]
            
            # Vistas aleatorias
            views = random.randint(0, 1000)
            
            post = Post.objects.create(
                title=title,
                body=body,
                author=random.choice(authors),
                category=random.choice(categories),
                status=status,
                published_at=published_at if status == 'published' else None,
                views=views if status == 'published' else 0
            )
            
            self.stdout.write(f'  - Created post: {post.title} ({post.status})')