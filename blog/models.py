from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return f"{self.name}"


ARTICLES_TYPES = [
    ("UN", "Unspecified"),
    ("TU", "Tutorial"),
    ("RW", "Review"),
    ("RS", "Research"),
]


class Article(models.Model):
    title = models.CharField(max_length=256)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    type = models.CharField(max_length=2, choices=ARTICLES_TYPES, default="UN")
    categories = models.ManyToManyField(
        to=Category, blank=True, related_name="categories"
    )
    content = models.TextField()
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author}:{self.title}({self.created_datetime.date()}"
