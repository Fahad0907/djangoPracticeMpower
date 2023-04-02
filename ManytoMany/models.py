from django.db import models

# Create your models here.
class Author(models.Model):
    name  = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
    
class Book(models.Model):
    name  = models.CharField(max_length=255)
    author_list = models.ManyToManyField(Author)

    def __str__(self) -> str:
        return self.name