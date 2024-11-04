from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title

class Article(models.Model):
    title = models.CharField(max_length=250)
    desc = models.TextField()
    image = models.ImageField(upload_to='article/', null=True, blank=True)
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)


