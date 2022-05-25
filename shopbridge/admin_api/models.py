from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField()
    price = models.PositiveIntegerField()
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name


class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    author = models.CharField(max_length=80)
    review = models.TextField(max_length=200)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)


