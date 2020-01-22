from django.db import models


# Create your models here.

class tags(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name


class Category(models.Model):
    title = models.CharField(max_length = 255)
    category = models.BooleanField(default = False)
    
    def __str__(self):
        return self.title

class Product(models.Model):
    name = models.CharField(max_length = 255)
    price = models.FloatField()
    slug = models.SlugField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    preview_text = models.TextField(max_length = 300, verbose_name='Preview Text')
    detail_text = models.TextField(max_length = 1000, verbose_name='Detail Text')
    image_url = models.CharField(max_length = 2083)
    tags = models.ManyToManyField(tags)
    
    
    def __str__(self):
        return self.name










