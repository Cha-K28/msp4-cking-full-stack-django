from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.TextField()
    author = models.TextField(max_length=254)
    subject = models.TextField(max_length=254)
    rating = models.DecimalField(max_digits=6, decimal_places=2,
                                 null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    year = models.CharField(max_length=254, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    grade = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name
