from django.db import models

class Author(models.Model):
    display_name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.display_name
