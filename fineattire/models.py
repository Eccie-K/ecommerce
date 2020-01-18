from django.db import models


# Create your models here.

class tags(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name



        
class Product(models.Model):
    name = models.CharField(max_length = 255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length = 2083)
    tags = models.ManyToManyField(tags)



class Offer(models.Model):
    code = models.CharField(max_length = 15)
    description = models.CharField(max_length =255)
    discount = models.FloatField()



